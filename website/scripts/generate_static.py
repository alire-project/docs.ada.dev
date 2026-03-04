#!/usr/bin/env python3
"""Generate static SEO pages for the Ada/SPARK documentation website.

Reads JSON data files produced by the gnatdoc JSON backend and writes
static HTML pages for:

  /                      → site/index.html
  /{crate}/              → site/{crate}/index.html
  /{crate}/{version}/    → site/{crate}/{version}/index.html

Unit pages (/{crate}/{version}/{unit}/) are rendered client-side by the
JS frontend and are NOT generated here.

Also copies website/frontend/ assets into site/assets/ so the full site
tree in site/ can be deployed directly to GitHub Pages.

Usage:
    python generate_static.py \\
        [--data DATA_DIR] \\
        [--output OUTPUT_DIR] \\
        [--templates TEMPLATES_DIR] \\
        [--frontend FRONTEND_DIR] \\
        [--base-url BASE_URL]

Defaults assume the script is run from the repo root or any directory; all
paths are relative to this script's location (website/scripts/).
"""

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from packaging.version import Version, InvalidVersion

try:
    import jinja2
except ImportError:
    print(
        "Error: jinja2 is required. Install with: pip install jinja2",
        file=sys.stderr,
    )
    sys.exit(1)

_SCRIPTS_DIR = Path(__file__).resolve().parent
_WEBSITE_DIR = _SCRIPTS_DIR.parent


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def load_json(path: Path) -> dict | None:
    """Load and return a JSON file, or None if not found / invalid."""
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        print(f"  Warning: {path} not found", file=sys.stderr)
        return None
    except json.JSONDecodeError as exc:
        print(f"  Warning: {path} is not valid JSON: {exc}", file=sys.stderr)
        return None


def top_level_units(units: list[dict]) -> list[str]:
    """Return unit names that have no dot (i.e. root packages only)."""
    return [u["name"] for u in units if "." not in u.get("name", "")]


def crate_documented_at(data_dir: Path, crate_entry: dict) -> str:
    """Return an ISO-8601 timestamp for when this crate was last documented.

    Preference order:
      1. documented_at in the global index entry (written by make_index.py).
      2. documented_at in the latest version's index.json.
      3. mtime of the latest version's index.json (fallback for older entries).
    """
    if "documented_at" in crate_entry:
        return crate_entry["documented_at"]
    latest = crate_entry.get("latest")
    if not latest:
        return ""
    path = data_dir / crate_entry["name"] / latest / "index.json"
    if not path.exists():
        return ""
    data = load_json(path)
    if data and "documented_at" in data:
        return data["documented_at"]
    # mtime fallback (reliable locally; unreliable after a git checkout)
    mtime = path.stat().st_mtime
    return datetime.fromtimestamp(mtime, tz=timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def rebuild_global_index(data_dir: Path) -> dict:
    """Rebuild global index from scratch by scanning all per-version manifests.

    Walks data/{crate}/{version}/index.json for every crate/version present in
    data_dir, builds the full crate list, and returns the index data structure.
    Metadata (description, tags, documented_at) is taken from each crate's
    latest version.
    """
    crates_map: dict[str, dict] = {}

    for index_file in sorted(data_dir.glob("*/*/index.json")):
        rel = index_file.relative_to(data_dir)
        if len(rel.parts) != 3:  # not crate/version/index.json
            continue
        crate_name, version = rel.parts[0], rel.parts[1]

        try:
            with open(index_file, encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception:
            continue

        if crate_name not in crates_map:
            crates_map[crate_name] = {"versions": [], "data": {}}
        crates_map[crate_name]["versions"].append(version)
        crates_map[crate_name]["data"][version] = data

    crates = []
    for crate_name in sorted(crates_map):
        entry = crates_map[crate_name]

        def version_key(v: str):
            try:
                return (0, Version(v))
            except InvalidVersion:
                # Fallback: treat invalid versions as greater than valid ones,
                # and sort lexicographically among themselves
                return (1, v)

        versions = sorted(entry["versions"], key=version_key)
        latest = versions[-1]
        latest_data = entry["data"].get(latest, {})
        crates.append(
            {
                "name": crate_name,
                "description": latest_data.get("description", ""),
                "tags": latest_data.get("tags", []),
                "documented_at": latest_data.get("documented_at", ""),
                "versions": versions,
                "latest": latest,
            }
        )

    global_index = {
        "schema_version": "1",
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "crates": crates,
    }

    print(f"  Rebuilt global index: {len(crates)} crate(s)")
    return global_index


# ---------------------------------------------------------------------------
# Core generator
# ---------------------------------------------------------------------------


def generate_static(
    data_dir: Path,
    output_dir: Path,
    templates_dir: Path,
    frontend_dir: Path,
    base_url: str,
) -> int:
    """Generate all static pages. Returns the number of pages written."""

    # --- Rebuild global index first ----------------------------------------
    print("Rebuilding global index...")
    index_data = rebuild_global_index(data_dir)

    schema_version = index_data.get("schema_version", "1")
    if schema_version != "1":
        print(
            f"Error: unsupported schema_version {schema_version!r} in index.json",
            file=sys.stderr,
        )
        return 0

    # --- Jinja2 environment ------------------------------------------------
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(templates_dir)),
        autoescape=jinja2.select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["base_url"] = base_url.rstrip("/")
    env.globals["now"] = datetime.now(timezone.utc).isoformat()

    output_dir.mkdir(parents=True, exist_ok=True)
    pages_written = 0

    # --- Global index page -------------------------------------------------
    crates = index_data.get("crates", [])
    recent_crates = sorted(
        crates,
        key=lambda c: crate_documented_at(data_dir, c),
        reverse=True,
    )[:10]
    tmpl = env.get_template("index.html.j2")
    html = tmpl.render(
        crates=crates,
        recent_crates=recent_crates,
        updated=index_data.get("updated", ""),
    )
    _write(output_dir / "index.html", html)
    pages_written += 1

    # --- Per-crate and per-version pages -----------------------------------
    for crate_entry in index_data.get("crates", []):
        crate_name = crate_entry["name"]
        versions = crate_entry.get("versions", [])
        latest = crate_entry.get("latest", versions[-1] if versions else "")

        # Load latest version manifest (for crate landing page)
        latest_manifest: dict | None = None
        if latest:
            latest_manifest = load_json(
                data_dir / crate_name / latest / "index.json"
            )

        # Crate page (one per crate — shows latest version with version switcher)
        crate_out = output_dir / crate_name
        crate_out.mkdir(parents=True, exist_ok=True)
        tmpl = env.get_template("crate.html.j2")
        html = tmpl.render(
            crate=crate_entry,
            latest_manifest=latest_manifest,
            top_level_units=top_level_units(
                latest_manifest.get("units", []) if latest_manifest else []
            ),
        )
        _write(crate_out / "index.html", html)
        pages_written += 1

    # --- Copy frontend assets ----------------------------------------------
    assets_out = output_dir / "assets"
    if frontend_dir.is_dir():
        if assets_out.exists():
            shutil.rmtree(assets_out)
        shutil.copytree(frontend_dir, assets_out)
        print(f"  Copied {frontend_dir} → {assets_out}")

        # Also place 404.html at the site root (GitHub Pages fallback for
        # client-side unit page routing).
        app_shell = frontend_dir / "index.html"
        if app_shell.exists():
            shutil.copy(app_shell, output_dir / "404.html")
            print(f"  Wrote  {output_dir / '404.html'}")
    else:
        print(
            f"  Warning: frontend directory {frontend_dir} not found; "
            "assets not copied",
            file=sys.stderr,
        )

    # --- Write global index to disk ----------------------------------------
    index_path = data_dir / "index.json"
    with open(index_path, "w", encoding="utf-8") as fh:
        json.dump(index_data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"  Wrote  {index_path}")

    # --- Link data directory into site tree --------------------------------
    # The JS frontend fetches /data/{crate}/{version}/{unit}.json at runtime,
    # so the data directory must be reachable under the site root.
    # We create a symlink site/data → data_dir if both are on the same
    # filesystem; otherwise we skip (CI can arrange the layout separately).
    data_link = output_dir / "data"
    if data_dir.is_dir():
        if data_link.exists() or data_link.is_symlink():
            data_link.unlink()
        try:
            data_link.symlink_to(data_dir.resolve())
            print(f"  Linked {data_link} → {data_dir.resolve()}")
        except OSError as exc:
            print(
                f"  Warning: could not symlink data directory: {exc}",
                file=sys.stderr,
            )

    return pages_written


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def _write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")
    print(f"  Wrote  {path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Generate static SEO pages for the Ada/SPARK documentation website."
        )
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=_WEBSITE_DIR / "data",
        metavar="DIR",
        help="Data directory (default: website/data/)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=_WEBSITE_DIR / "site",
        metavar="DIR",
        help="Output directory (default: website/site/)",
    )
    parser.add_argument(
        "--templates",
        type=Path,
        default=_WEBSITE_DIR / "templates",
        metavar="DIR",
        help="Templates directory (default: website/templates/)",
    )
    parser.add_argument(
        "--frontend",
        type=Path,
        default=_WEBSITE_DIR / "frontend",
        metavar="DIR",
        help="Frontend source directory (default: website/frontend/)",
    )
    parser.add_argument(
        "--base-url",
        default="",
        metavar="URL",
        help="Base URL for the site (e.g. https://user.github.io/repo)",
    )
    args = parser.parse_args()

    print(f"Data directory:    {args.data}")
    print(f"Output directory:  {args.output}")
    print(f"Templates:         {args.templates}")
    print(f"Frontend:          {args.frontend}")
    if args.base_url:
        print(f"Base URL:          {args.base_url}")
    print()

    count = generate_static(
        args.data,
        args.output,
        args.templates,
        args.frontend,
        args.base_url,
    )
    print(f"\nDone — {count} page(s) generated.")


if __name__ == "__main__":
    main()
