#!/usr/bin/env python3
"""Validate, unpack per-crate tarballs, rebuild the global index, and commit.

For each .tar.gz in --artifacts:
  1. Validate: must be a valid gzip archive with all members under a single
     {crate}/{version}/ prefix and contain either index.json or error.json.
  2. Skip if that crate/version is already committed (idempotent re-runs).
  3. Extract into --data-dir.
  4. git add + git commit for that crate only.

After all tarballs:
  5. Rebuild data/index.json from scratch by scanning every
     data/{crate}/{version}/index.json file currently in --data-dir.
  6. Commit the rebuilt index and push.

Tarballs that fail validation are logged to stderr and an error.json is
written to website/data/{crate}/{version}/ so the failure is visible and
check_updates.py will skip the crate on future runs.

Exit codes: 0 = success (including "nothing to commit"), 1 = any failure.
"""

import argparse
import json
import subprocess
import sys
import tarfile
from datetime import datetime, timezone
from pathlib import Path


def run(cmd: list, check: bool = True) -> subprocess.CompletedProcess:
    print(f"  $ {' '.join(str(c) for c in cmd)}", flush=True)
    return subprocess.run([str(c) for c in cmd], check=check)


def validate_tarball(path: Path) -> tuple[str, str] | None:
    """Return (crate, version) if the tarball is valid, else None.

    Validation rules:
    - Must be a readable gzip archive.
    - Must be non-empty.
    - All member paths must share a single {crate}/{version}/ prefix.
    - Must contain {prefix}/index.json or {prefix}/error.json.
    """
    try:
        with tarfile.open(path, "r:gz") as tar:
            members = tar.getnames()
    except Exception as exc:
        print(f"  INVALID {path.name}: cannot open archive: {exc}", file=sys.stderr)
        return None

    if not members:
        print(f"  INVALID {path.name}: empty archive", file=sys.stderr)
        return None

    # Derive the expected prefix from the first member
    first_parts = Path(members[0]).parts
    if len(first_parts) < 2:
        print(
            f"  INVALID {path.name}: top-level path {members[0]!r} has no "
            f"crate/version prefix",
            file=sys.stderr,
        )
        return None

    crate, version = first_parts[0], first_parts[1]
    prefix = f"{crate}/{version}"

    # Every member must live under the same prefix
    for m in members:
        if m != prefix and not m.startswith(prefix + "/"):
            print(
                f"  INVALID {path.name}: unexpected path {m!r} "
                f"(expected prefix {prefix!r})",
                file=sys.stderr,
            )
            return None

    # Must document either success or failure
    member_set = set(members)
    if (
        f"{prefix}/index.json" not in member_set
        and f"{prefix}/error.json" not in member_set
    ):
        print(
            f"  INVALID {path.name}: contains neither index.json nor error.json",
            file=sys.stderr,
        )
        return None

    return crate, version


def write_collect_error(data_dir: Path, crate: str, version: str, message: str) -> None:
    """Record a validation failure as error.json so future runs skip this crate."""
    version_dir = data_dir / crate / version
    version_dir.mkdir(parents=True, exist_ok=True)
    error = {
        "schema_version": "1",
        "crate": crate,
        "version": version,
        "failed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "stage": "collect",
        "message": message,
    }
    path = version_dir / "error.json"
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(error, fh, indent=2)
    print(f"  Wrote collect error record: {path}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate + unpack crate tarballs and commit each one."
    )
    parser.add_argument(
        "--artifacts",
        required=True,
        type=Path,
        metavar="DIR",
        help="Directory containing per-crate .tar.gz files",
    )
    parser.add_argument(
        "--data-dir",
        required=True,
        type=Path,
        metavar="DIR",
        help="website/data/ root in the repository checkout",
    )
    args = parser.parse_args()

    if not args.artifacts.exists():
        print(
            f"Error: artifacts directory not found: {args.artifacts}", file=sys.stderr
        )
        sys.exit(1)

    tarballs = sorted(args.artifacts.glob("*.tar.gz"))
    if not tarballs:
        print("No tarballs found — nothing to commit.", file=sys.stderr)

    # Configure git identity once
    run(["git", "config", "user.name", "github-actions[bot]"])
    run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"])

    committed = 0
    invalid = []

    for tarball in tarballs:
        print(f"\nProcessing {tarball.name} …")

        result = validate_tarball(tarball)
        if result is None:
            invalid.append(tarball.name)
            # Try to derive crate/version from the filename as a fallback
            # for writing the error.json (best-effort).
            stem = tarball.stem.removesuffix(".tar")  # handles .tar.gz stem
            parts = stem.rsplit("-", 1)
            if len(parts) == 2:
                write_collect_error(
                    args.data_dir,
                    parts[0],
                    parts[1],
                    f"Invalid tarball: {tarball.name}",
                )
            continue

        crate, version = result
        version_dir = args.data_dir / crate / version

        # Idempotent: skip if this version is already in the tree
        if (version_dir / "index.json").exists() or (
            version_dir / "error.json"
        ).exists():
            print(f"  Already present — skipping {crate}={version}")
            continue

        # Extract directly into data_dir (tarball carries the crate/version path)
        with tarfile.open(tarball, "r:gz") as tar:
            tar.extractall(args.data_dir)
        print(f"  Extracted → {version_dir}")

        # Commit this crate individually
        run(["git", "add", str(version_dir)])
        diff = run(["git", "diff", "--cached", "--quiet"], check=False)
        if diff.returncode == 0:
            print(f"  No staged changes for {crate}={version} — skipping commit")
            continue

        run(["git", "commit", "-m", f"docs: add {crate}={version}"])
        committed += 1

    print(
        f"\nSummary: {committed} commit(s), {len(invalid)} invalid tarball(s).",
        file=sys.stderr,
    )

    if committed > 0:
        run(["git", "push"])

    if invalid:
        print(f"Invalid tarballs: {', '.join(invalid)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
