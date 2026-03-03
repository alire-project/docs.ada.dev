#!/usr/bin/env python3
"""Full documentation pipeline for a single Alire crate.

Steps:
  1. alr get {crate}={version}  — fetch sources into a temp directory
  2. Locate the crate root      — handles nested crates (monorepo layout)
  3. alr build                  — generate config/ and compile
  4. alr exec -P -- gnatdoc … --backend json  — produce unit JSON files
  5. make_index.py              — create the index.json manifest

On success, data/{crate}/{version}/index.json is written.
On failure at any stage, data/{crate}/{version}/error.json is written with
the stage name, error message, and timestamp so that:
  - check_updates.py skips the crate on future runs (no endless retries).
  - The error is visible in the data/ directory for diagnosis.

To retry a failed crate, delete its error.json and re-run.

Usage:
    python3 process_crate.py \\
        --crate           CRATE    \\   # e.g. midi
        --version         VERSION  \\   # e.g. 1.0.0
        --data-dir        DIR      \\   # website/data/
        --gnatdoc         PATH     \\   # path to the gnatdoc binary
        [--output-tarball PATH]         # pack output into a .tar.gz for CI upload
        [--work-dir       DIR]          # temp dir for alr get (default: auto)
        [--keep-work]                   # don't delete work dir on success

Exit codes: 0 = success (or already processed), 1 = failure.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# Subprocess helpers
# ---------------------------------------------------------------------------

def run(cmd: list, cwd: Path | None = None, env: dict | None = None,
        check: bool = True) -> subprocess.CompletedProcess:
    """Run a command, streaming output to stdout/stderr."""
    print(f"  $ {' '.join(str(c) for c in cmd)}", flush=True)
    return subprocess.run(
        [str(c) for c in cmd],
        cwd=str(cwd) if cwd else None,
        env=env,
        check=check,
    )


# ---------------------------------------------------------------------------
# Error recording
# ---------------------------------------------------------------------------

def write_error(data_dir: Path, crate: str, version: str,
                stage: str, message: str) -> None:
    """Write data/{crate}/{version}/error.json recording a pipeline failure."""
    output_dir = data_dir / crate / version
    output_dir.mkdir(parents=True, exist_ok=True)

    error = {
        "schema_version": "1",
        "crate":      crate,
        "version":    version,
        "failed_at":  datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "stage":      stage,
        "message":    message,
    }
    path = output_dir / "error.json"
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(error, fh, indent=2)
    print(f"  Wrote error record: {path}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Crate directory discovery
# ---------------------------------------------------------------------------

def find_crate_dir(work_dir: Path, crate: str, version: str) -> Path:
    """
    After 'alr get {crate}={version}' has run in *work_dir*, find the
    directory that contains the crate's alire.toml.

    alr get produces one of two layouts:

      Non-nested:
        {crate}_{version}_{hash}/     ← crate root, contains alire.toml

      Nested (monorepo):
        {crate}_{version}_in_{hash}   ← empty marker file
        {hash}/                        ← git repo root
          {subdir}/                    ← actual crate root, contains alire.toml

    We identify the crate root as the directory inside work_dir that
    contains an alire.toml whose 'name' field matches *crate*.
    """
    # Fast path: direct directory
    for entry in work_dir.iterdir():
        if not entry.is_dir():
            continue
        toml = entry / "alire.toml"
        if toml.exists() and _toml_name(toml) == crate:
            return entry

    # Nested path: search one level deeper inside any new directory
    for entry in work_dir.iterdir():
        if not entry.is_dir():
            continue
        for sub in entry.iterdir():
            if not sub.is_dir():
                continue
            toml = sub / "alire.toml"
            if toml.exists() and _toml_name(toml) == crate:
                return sub

    raise RuntimeError(
        f"Could not find crate root for {crate}={version} in {work_dir}"
    )


def _toml_name(toml_path: Path) -> str:
    """Extract the 'name' field from an alire.toml without a full TOML parser."""
    text = toml_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("name"):
            parts = line.split("=", 1)
            if len(parts) == 2:
                return parts[1].strip().strip('"\'')
    return ""


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

# Names used in error.json "stage" field — one per pipeline step.
_STAGE_FETCH   = "fetch"
_STAGE_LOCATE  = "locate"
_STAGE_BUILD   = "build"
_STAGE_GNATDOC = "gnatdoc"
_STAGE_INDEX   = "index"


def process_crate(
    crate: str,
    version: str,
    data_dir: Path,
    gnatdoc: Path,
    work_dir: Path,
    force: bool = False,
) -> None:
    output_dir = data_dir / crate / version

    # Skip if already successfully processed
    if (output_dir / "index.json").exists():
        print(f"  Already processed — skipping {crate}={version}")
        return

    # Skip previous failures unless --force was given
    error_file = output_dir / "error.json"
    if error_file.exists():
        if not force:
            print(f"  Previous failure recorded — skipping {crate}={version} "
                  f"(use --force to retry)")
            return
        error_file.unlink()
        print(f"  Removed previous error.json — retrying {crate}={version}")

    print(f"\n{'='*60}")
    print(f"  Processing {crate}={version}")
    print(f"{'='*60}\n")

    # 1. Fetch crate sources
    try:
        run(["alr", "get", f"{crate}={version}"], cwd=work_dir)
    except subprocess.CalledProcessError as exc:
        write_error(data_dir, crate, version, _STAGE_FETCH,
                    f"alr get exited with code {exc.returncode}")
        raise

    # 2. Locate crate root
    try:
        crate_dir = find_crate_dir(work_dir, crate, version)
        print(f"  Crate root: {crate_dir}")
    except RuntimeError as exc:
        write_error(data_dir, crate, version, _STAGE_LOCATE, str(exc))
        raise

    # 3. Generate config/ files (no compilation needed for documentation)
    try:
        run(["alr", "build", "--stop-after=generation"], cwd=crate_dir)
    except subprocess.CalledProcessError as exc:
        write_error(data_dir, crate, version, _STAGE_BUILD,
                    f"alr build exited with code {exc.returncode}")
        raise

    # 4. Run gnatdoc JSON backend
    output_dir.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["GNATDOC_CRATE"]   = crate
    env["GNATDOC_VERSION"] = version
    try:
        run(
            ["alr", "exec", "-P", "--",
             str(gnatdoc.resolve()),
             "--backend", "json",
             "--output-dir", str(output_dir.resolve())],
            cwd=crate_dir,
            env=env,
        )
    except subprocess.CalledProcessError as exc:
        write_error(data_dir, crate, version, _STAGE_GNATDOC,
                    f"gnatdoc exited with code {exc.returncode}")
        raise

    # 5. Generate index.json manifest
    make_index = _SCRIPTS_DIR / "make_index.py"
    try:
        run(
            [sys.executable, str(make_index),
             "--data-dir",  str(data_dir.resolve()),
             "--crate",     crate,
             "--version",   version],
        )
    except subprocess.CalledProcessError as exc:
        write_error(data_dir, crate, version, _STAGE_INDEX,
                    f"make_index.py exited with code {exc.returncode}")
        raise

    print(f"\n  Done: {crate}={version}\n")


# ---------------------------------------------------------------------------
# Output packaging
# ---------------------------------------------------------------------------

def package_output(output_dir: Path, crate: str, version: str,
                   tarball_path: Path) -> None:
    """Pack data/{crate}/{version}/ into a gzip tarball for CI artifact upload.

    The archive uses {crate}/{version}/ as the top-level prefix so that
    ci_collect.py can validate the structure and extract directly into
    website/data/ without extra path manipulation.

    Skips (with a warning) if neither index.json nor error.json is present,
    which would indicate the pipeline exited without writing any output.
    """
    has_index = (output_dir / "index.json").exists()
    has_error = (output_dir / "error.json").exists()

    if not has_index and not has_error:
        print(
            f"  Warning: {output_dir} contains neither index.json nor "
            "error.json — skipping tarball creation.",
            file=sys.stderr,
        )
        return

    tarball_path.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(tarball_path, "w:gz") as tar:
        tar.add(output_dir, arcname=f"{crate}/{version}")

    status = "success" if has_index else "error"
    n = sum(1 for f in output_dir.rglob("*") if f.is_file())
    print(f"  Packaged {crate}={version} ({status}, {n} file(s)) → {tarball_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the full documentation pipeline for one Alire crate."
    )
    parser.add_argument("--crate",     required=True, help="Crate name (e.g. midi)")
    parser.add_argument("--version",   required=True, help="Version (e.g. 1.0.0)")
    parser.add_argument("--data-dir",  required=True, type=Path,
                        help="website/data/ root")
    parser.add_argument("--gnatdoc",   required=True, type=Path,
                        help="Path to the gnatdoc binary")
    parser.add_argument("--output-tarball", type=Path, default=None, metavar="PATH",
                        help="Pack data/{crate}/{version}/ into this .tar.gz after "
                             "processing (for CI artifact upload)")
    parser.add_argument("--work-dir",  type=Path, default=None,
                        help="Working directory for alr get (default: auto temp dir)")
    parser.add_argument("--keep-work", action="store_true",
                        help="Keep work directory after completion")
    parser.add_argument("--force", action="store_true",
                        help="Retry even if a previous error.json exists")
    args = parser.parse_args()

    if not args.gnatdoc.exists():
        print(f"Error: gnatdoc binary not found: {args.gnatdoc}", file=sys.stderr)
        sys.exit(1)

    own_work_dir = args.work_dir is None
    work_dir = args.work_dir or Path(tempfile.mkdtemp(prefix="gnatdoc_"))

    failed = False
    try:
        process_crate(
            crate=args.crate,
            version=args.version,
            data_dir=args.data_dir,
            gnatdoc=args.gnatdoc,
            work_dir=work_dir,
            force=args.force,
        )
    except (subprocess.CalledProcessError, RuntimeError):
        # Error already recorded in error.json and printed to stderr.
        failed = True
    except Exception as exc:
        # Unexpected error — record it too.
        write_error(args.data_dir, args.crate, args.version,
                    "unknown", str(exc))
        print(f"\nUnexpected error: {exc}", file=sys.stderr)
        failed = True
    finally:
        if own_work_dir and not args.keep_work:
            shutil.rmtree(work_dir, ignore_errors=True)

    if args.output_tarball:
        package_output(
            output_dir=args.data_dir / args.crate / args.version,
            crate=args.crate,
            version=args.version,
            tarball_path=args.output_tarball,
        )

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
