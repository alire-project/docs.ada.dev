#!/usr/bin/env python3
"""Diff the available Alire crates against website/data/ to find what is
not yet documented.

Uses 'alr --format=JSON search --list' to enumerate all available crates
(one entry per crate, at its latest indexed version).  A crate version is
considered "processed" when data/{crate}/{version}/index.json exists.

Output modes (--format):
  text    One "crate=version" line per missing entry (default for humans).
  json    JSON array: [{"crate": "...", "version": "..."}, ...]
  chunks  JSON matrix for GitHub Actions parallel jobs:
            [{"chunk_id": 0, "crates": "crate1=1.0.0 crate2=2.0.0"}, ...]
          Use with --chunks N to control parallelism.

Usage:
    python3 check_updates.py \\
        --data    website/data/  \\
        [--format text|json|chunks] \\
        [--chunks N]             \\   # number of parallel chunks (default 10)
        [--limit  N]             \\
        [--crate  NAME]          \\   # restrict output to one crate
        [--retry-errors]             # include previously-failed crates
"""

import argparse
import json
import math
import subprocess
import sys
from pathlib import Path


def list_alire_crates() -> list[dict]:
    """Run 'alr --format=JSON search --list' and return the parsed array."""
    result = subprocess.run(
        ["alr", "--format=JSON", "search", "--list"],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def is_processed(data_dir: Path, crate: str, version: str) -> bool:
    """Return True if this crate version has been successfully documented
    OR if a failure has already been recorded (error.json)."""
    version_dir = data_dir / crate / version
    return (
        (version_dir / "index.json").exists()
        or (version_dir / "error.json").exists()
    )


def find_missing(
    data_dir: Path,
    crate_filter: str | None = None,
    limit: int | None = None,
    include_errors: bool = False,
) -> list[dict]:
    """Return list of {"crate": ..., "version": ...} not yet processed.

    If *include_errors* is True, crates with an error.json are re-included
    so they will be retried (useful after fixing a known issue).
    """
    crates = list_alire_crates()
    missing = []
    for entry in crates:
        crate   = entry["name"]
        version = entry["version"]
        if crate_filter and crate != crate_filter:
            continue
        version_dir = data_dir / crate / version
        already_ok    = (version_dir / "index.json").exists()
        already_error = (version_dir / "error.json").exists()
        if already_ok:
            continue
        if already_error and not include_errors:
            continue
        missing.append({
            "crate":       crate,
            "version":     version,
            "description": entry.get("description", ""),
        })
        if limit and len(missing) >= limit:
            break
    return missing


def make_chunks(items: list[dict], n_chunks: int) -> list[dict]:
    """Split *items* into at most *n_chunks* roughly equal groups.

    Returns a list of {"chunk_id": N, "crates": "crate1=v1 crate2=v2 ..."}
    dicts suitable as a GitHub Actions matrix.  Empty chunks are omitted, so
    if there are fewer items than n_chunks the returned list is shorter.
    """
    if not items:
        return []
    # Clamp: never create more chunks than items
    n = min(n_chunks, len(items))
    size = math.ceil(len(items) / n)
    chunks = []
    for i in range(0, len(items), size):
        batch = items[i : i + size]
        chunks.append({
            "chunk_id": len(chunks),
            # Space-separated "crate=version" tokens, easy to split in bash
            "crates": " ".join(f"{e['crate']}={e['version']}" for e in batch),
        })
    return chunks


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find Alire crates not yet documented in website/data/."
    )
    parser.add_argument(
        "--data", required=True, type=Path, metavar="DIR",
        help="website/data/ root",
    )
    parser.add_argument(
        "--format", choices=["text", "json", "chunks"], default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--chunks", type=int, default=10, metavar="N",
        help="Number of parallel chunks for --format=chunks (default: 10)",
    )
    parser.add_argument(
        "--limit", type=int, default=None, metavar="N",
        help="Maximum number of crates to include across all output",
    )
    parser.add_argument(
        "--crate", default=None, metavar="NAME",
        help="Restrict output to a single crate name",
    )
    parser.add_argument(
        "--retry-errors", action="store_true",
        help="Include crates that previously failed (have error.json)",
    )
    args = parser.parse_args()

    try:
        missing = find_missing(
            data_dir=args.data,
            crate_filter=args.crate,
            limit=args.limit,
            include_errors=args.retry_errors,
        )
    except subprocess.CalledProcessError as exc:
        print(f"Error: 'alr search --list' failed: {exc}", file=sys.stderr)
        sys.exit(1)

    if args.format == "chunks":
        print(json.dumps(make_chunks(missing, args.chunks), indent=2))
    elif args.format == "json":
        print(json.dumps(
            [{"crate": e["crate"], "version": e["version"]} for e in missing],
            indent=2,
        ))
    else:
        for e in missing:
            print(f"{e['crate']}={e['version']}")

    if not missing:
        print("All indexed crates are up to date.", file=sys.stderr)


if __name__ == "__main__":
    main()
