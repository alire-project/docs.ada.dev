#!/usr/bin/env python3
"""Compute the GitHub Actions work matrix for the process-crates workflow.

Calls check_updates to find pending crates and writes the results in
GitHub Actions output variable format so the workflow can redirect stdout
directly to $GITHUB_OUTPUT:

    python3 ci_prepare.py [options] >> $GITHUB_OUTPUT

Output lines written to stdout:
    matrix=<JSON array of {"crate": "...", "version": "..."} objects>
    has_work=true|false

Usage:
    python3 ci_prepare.py \\
        --data     website/data \\
        --limit    100          \\
        [--crate   NAME=VERSION] \\
        [--retry-errors]

Can also be run locally — it just prints to stdout in that case.
"""

import argparse
import json
import sys
from pathlib import Path

# Import siblings without installing as a package
sys.path.insert(0, str(Path(__file__).parent))
from check_updates import find_missing


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute CI work matrix for process-crates workflow."
    )
    parser.add_argument(
        "--data", required=True, type=Path, metavar="DIR",
        help="website/data/ root",
    )
    parser.add_argument(
        "--limit", type=int, default=100, metavar="N",
        help="Maximum number of crates to include (default: 100)",
    )
    parser.add_argument(
        "--crate", default=None, metavar="NAME=VERSION",
        help="Process a single specific crate (e.g. midi=1.0.0)",
    )
    parser.add_argument(
        "--retry-errors", action="store_true",
        help="Include crates that previously failed",
    )
    args = parser.parse_args()

    if args.crate:
        # Single crate: one-element matrix
        if "=" not in args.crate:
            print(f"Error: --crate must be NAME=VERSION, got {args.crate!r}",
                  file=sys.stderr)
            sys.exit(1)
        name, version = args.crate.split("=", 1)
        matrix = [{"crate": name, "version": version}]
    else:
        missing = find_missing(
            data_dir=args.data,
            limit=args.limit,
            include_errors=args.retry_errors,
        )
        matrix = [{"crate": e["crate"], "version": e["version"]} for e in missing]

    has_work = len(matrix) > 0
    print(f"matrix={json.dumps(matrix)}")
    print(f"has_work={str(has_work).lower()}")

    if not has_work:
        print("No new crates to process.", file=sys.stderr)
    else:
        print(f"{len(matrix)} crate(s) to process.", file=sys.stderr)


if __name__ == "__main__":
    main()
