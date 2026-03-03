#!/usr/bin/env python3
"""Create (or update) the index.json manifest files after a gnatdoc JSON run.

For a given crate, this script:
  1. Runs 'alr --format=JSON show {crate}={version}' to get metadata.
  2. Scans the gnatdoc JSON output directory and identifies which unit files
     belong to the crate itself (vs. its dependencies).  Units whose source
     file path is relative and does not start with "../" are crate-owned;
     absolute paths and "../"-prefixed paths are dependency units.
  3. Writes  data/{crate}/{version}/index.json
  4. Regenerates  data/index.json  to include the crate (adds or updates the
     entry for this crate/version).

Usage:
    python3 make_index.py \\
        --data-dir   DATA_DIR    \\   # website/data/ root
        --crate      CRATE_NAME  \\   # e.g. midi
        --version    VERSION         # e.g. 1.0.0
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# alr metadata
# ---------------------------------------------------------------------------

def alr_show(crate: str, version: str) -> dict:
    """Run 'alr --format=JSON show {crate}={version}' and return the result."""
    result = subprocess.run(
        ["alr", "--format=JSON", "show", f"{crate}={version}"],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


# ---------------------------------------------------------------------------
# JSON helpers
# ---------------------------------------------------------------------------

def load_json(path: Path) -> dict | None:
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
    print(f"  Wrote  {path}")


# ---------------------------------------------------------------------------
# Core: identify which unit files belong to the crate
# ---------------------------------------------------------------------------

def collect_crate_units(json_dir: Path) -> list[dict]:
    """
    Scan *json_dir* for unit JSON files and return those whose source file
    is located inside *crate_root* (i.e. they belong to the crate, not a
    dependency).

    The gnatdoc JSON backend now writes paths relative to the crate root.
    A unit belongs to the crate when its path is relative and does not
    escape the root (i.e. does not start with "../").  Absolute paths and
    "../"-prefixed paths indicate dependency units and are excluded.

    Returns a list of {"name": ..., "id": ..., "file": ...} dicts sorted by
    name, ready for inclusion in the index.json units array.
    """
    units = []

    for json_file in sorted(json_dir.glob("*.json")):
        data = load_json(json_file)
        if data is None:
            continue

        src_file = (data.get("location") or {}).get("file", "")
        # Relative path that stays inside the crate root: belongs to crate.
        # Absolute path or "../"-prefixed path: dependency unit, skip.
        if not src_file or src_file.startswith("/") or src_file.startswith("../"):
            continue

        units.append({
            "name": data.get("qualified_name") or data.get("name", json_file.stem),
            "id":   data.get("id", ""),
            "file": json_file.name,
        })

    units.sort(key=lambda u: u["name"].lower())
    return units


# ---------------------------------------------------------------------------
# Core: parse dependencies from the alr show output
# ---------------------------------------------------------------------------

def parse_dependencies(manifest: dict) -> list[dict]:
    deps = []
    for block in manifest.get("depends-on", []):
        if not isinstance(block, dict):
            continue
        for crate, version_spec in block.items():
            if crate in ("gnat", "gprbuild"):
                continue
            deps.append({"crate": crate, "version": str(version_spec)})
    return deps


# ---------------------------------------------------------------------------
# Core: detect source repository from alr metadata
# ---------------------------------------------------------------------------

def detect_source_repo(manifest: dict) -> dict | None:
    """Heuristically identify the source repository from alr show metadata.

    Tries in order:
      1. manifest["origin"]["url"]  — git clone URL or release archive URL
      2. manifest["website"]        — project website (accepted only when it
                                      resolves to a recognised forge)

    Returns a dict such as:
        {"url": "https://github.com/owner/repo",
         "host": "github",
         "commit": "abc123...",   # present when origin has a commit SHA
         "subdir": "sub/dir/"}    # present when origin has a subdir
    or None if no recognisable repository URL can be found.
    """
    origin = manifest.get("origin") or {}
    commit = origin.get("commit", "")
    subdir = _normalize_subdir(origin.get("subdir", ""))

    # Primary: origin URL (always a source location)
    repo_url = _clean_repo_url(origin.get("url", ""))

    # Fallback: website field — accepted only when it is on a known forge
    if not repo_url:
        ws = _clean_repo_url(manifest.get("website", ""))
        if ws and _detect_host(ws) != "git":
            repo_url = ws

    if not repo_url:
        return None

    result: dict = {"url": repo_url, "host": _detect_host(repo_url)}
    if commit:
        result["commit"] = commit
    if subdir:
        result["subdir"] = subdir
    return result


def _clean_repo_url(url: str) -> str:
    """Return a canonical repository root URL, or '' if not recognisable."""
    if not url:
        return ""
    # Strip git+ transport prefix
    url = re.sub(r"^git\+", "", url)
    # Strip trailing .git (case-insensitive)
    url = re.sub(r"\.git$", "", url, flags=re.IGNORECASE)
    # For known forges extract scheme://host/owner/repo (first two path segments)
    for host in (
        "github.com",
        "gitlab.com",
        "codeberg.org",
        "bitbucket.org",
        "sourceforge.net",
    ):
        m = re.match(
            rf"(https?://{re.escape(host)}/[^/?#\s]+/[^/?#\s]+)(/.*)?$", url
        )
        if m:
            return m.group(1)
    # Unknown host: accept any https:// URL, stripping query/fragment
    m = re.match(r"(https?://\S+?)[\s/?#]*$", url)
    if m:
        return m.group(1).rstrip("/")
    return ""


def _normalize_subdir(subdir: str) -> str:
    """Normalise an alire origin.subdir value to 'path/prefix/' or ''."""
    if not subdir:
        return ""
    subdir = subdir.strip()
    # Remove leading "./" prefix(es) and slashes
    while subdir.startswith("./"):
        subdir = subdir[2:]
    subdir = subdir.strip("/")
    return (subdir + "/") if subdir else ""


def _detect_host(url: str) -> str:
    """Return a short host identifier for a repository URL."""
    lower = url.lower()
    for fragment, label in (
        ("github.com",      "github"),
        ("gitlab.com",      "gitlab"),
        ("codeberg.org",    "codeberg"),
        ("bitbucket.org",   "bitbucket"),
        ("sourceforge.net", "sourceforge"),
    ):
        if fragment in lower:
            return label
    return "git"


# ---------------------------------------------------------------------------
# Core: write data/{crate}/{version}/index.json
# ---------------------------------------------------------------------------

def write_version_index(
    data_dir: Path,
    crate_name: str,
    version: str,
    manifest: dict,
    units: list[dict],
) -> None:
    index = {
        "schema_version":   "1",
        "crate":            crate_name,
        "version":          version,
        "documented_at":    datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "description":      manifest.get("description", ""),
        "long_description": manifest.get("long-description", ""),
        "authors":          manifest.get("authors", []),
        "licenses":         _as_list(manifest.get("licenses", [])),
        "tags":             manifest.get("tags", []),
        "website":          manifest.get("website", ""),
        "repository":       detect_source_repo(manifest),
        "dependencies":     parse_dependencies(manifest),
        "units":            units,
    }

    # Drop empty/None optional fields
    for key in ("long_description", "website", "repository"):
        if not index[key]:
            del index[key]

    write_json(data_dir / crate_name / version / "index.json", index)


# ---------------------------------------------------------------------------
# Core: update data/index.json
# ---------------------------------------------------------------------------

def update_global_index(
    data_dir: Path,
    crate_name: str,
    version: str,
    manifest: dict,
) -> None:
    global_path = data_dir / "index.json"
    global_index = load_json(global_path) or {
        "schema_version": "1",
        "updated": "",
        "crates": [],
    }

    crates: list[dict] = global_index.setdefault("crates", [])
    entry = next((c for c in crates if c["name"] == crate_name), None)
    if entry is None:
        entry = {"name": crate_name, "versions": []}
        crates.append(entry)

    entry["description"]   = manifest.get("description", "")
    entry["tags"]          = manifest.get("tags", [])
    entry["documented_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if version not in entry["versions"]:
        entry["versions"].append(version)
    entry["versions"] = sorted(
        entry["versions"],
        key=lambda v: [int(x) for x in v.split(".")],
    )
    entry["latest"] = entry["versions"][-1]

    crates.sort(key=lambda c: c["name"])
    global_index["updated"] = datetime.now(timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    write_json(global_path, global_index)


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def _as_list(value) -> list:
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        return [value]
    return []


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create index.json manifest files for a crate after a gnatdoc run."
    )
    parser.add_argument(
        "--data-dir", required=True, type=Path, metavar="DIR",
        help="Root of website/data/",
    )
    parser.add_argument(
        "--crate", required=True, metavar="NAME",
        help="Alire crate name (e.g. midi)",
    )
    parser.add_argument(
        "--version", required=True, metavar="VER",
        help="Crate version (e.g. 1.0.0)",
    )
    args = parser.parse_args()

    json_dir = args.data_dir / args.crate / args.version
    if not json_dir.is_dir():
        print(f"Error: JSON output directory {json_dir} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching metadata via alr show {args.crate}={args.version}")
    try:
        manifest = alr_show(args.crate, args.version)
    except subprocess.CalledProcessError as exc:
        print(f"Error: alr show failed: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"JSON dir:    {json_dir}")
    print()

    units = collect_crate_units(json_dir)
    print(f"  Found {len(units)} crate unit(s) (dependency units excluded from index)")
    for u in units:
        print(f"    {u['name']}")

    print()
    write_version_index(args.data_dir, args.crate, args.version, manifest, units)
    update_global_index(args.data_dir, args.crate, args.version, manifest)

    print("\nDone.")


if __name__ == "__main__":
    main()
