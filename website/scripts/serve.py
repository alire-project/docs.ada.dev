#!/usr/bin/env python3
"""Local dev server for the Ada/SPARK documentation website.

Simulates GitHub Pages behaviour:
  - Serves files from website/site/ (follows symlinks, so site/data/ works).
  - For a directory URL, tries index.html inside it.
  - For any path that doesn't match a real file, serves site/404.html with
    status 200 — exactly how GitHub Pages delivers the SPA fallback for
    client-side unit page routing.

Usage:
    python3 website/scripts/serve.py [--port PORT] [--host HOST]

Defaults: host=0.0.0.0 (accessible from outside the container), port=8080.
"""

import argparse
import http.server
import os
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
_SITE_DIR    = _SCRIPTS_DIR.parent / "site"


class SPAHandler(http.server.SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler with SPA 404→index fallback."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(_SITE_DIR), **kwargs)

    def do_GET(self):
        # Resolve the requested path to a filesystem path.
        # SimpleHTTPRequestHandler.translate_path() handles URL-decoding,
        # query strings, and path traversal.
        fs_path = Path(self.translate_path(self.path))

        # Try directory index
        if fs_path.is_dir():
            index = fs_path / "index.html"
            if index.exists():
                # Let the parent handle it normally.
                return super().do_GET()

        # File exists — serve it normally (covers assets, JSON data, etc.)
        if fs_path.is_file():
            return super().do_GET()

        # Nothing matched — serve 404.html with status 200 (GitHub Pages SPA
        # fallback).  app.js will read window.location and render the unit.
        fallback = _SITE_DIR / "404.html"
        if not fallback.exists():
            self.send_error(404, "404.html not found in site root")
            return

        content = fallback.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, fmt, *args):
        # Quieter log: omit the date prefix that SimpleHTTPRequestHandler adds.
        print(f"  {self.address_string()}  {fmt % args}")


def main():
    parser = argparse.ArgumentParser(description="Local dev server for the docs site.")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--host", default="0.0.0.0",
                        help="Bind address (default 0.0.0.0 — accessible outside container)")
    args = parser.parse_args()

    if not _SITE_DIR.exists():
        print(f"Error: site directory not found: {_SITE_DIR}")
        print("Run  python3 website/scripts/generate_static.py  first.")
        raise SystemExit(1)

    print(f"Serving {_SITE_DIR}")
    print(f"Open:   http://localhost:{args.port}/")
    print("Ctrl-C to stop.\n")

    with http.server.HTTPServer((args.host, args.port), SPAHandler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    main()
