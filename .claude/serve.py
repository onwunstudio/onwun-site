"""Local preview server for the site: like `python3 -m http.server`, but tells the browser not to cache,
so a normal refresh always shows the latest files; answers range requests (part of a file), which
iPhone Safari needs to play and loop videos; and understands the same clean addresses as vercel.json
(/about, /projects/atlas). For local previewing only."""

import http.server
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


PROJECTS = ("atlas", "denglish", "elev8", "rise", "stuartfox")


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def translate_path(self, path):
        """The same addresses as vercel.json on the live site: /projects/atlas serves atlas.html, and
        /about serves about.html (clean URLs)."""
        clean = path.split("?", 1)[0].split("#", 1)[0].rstrip("/")
        parts = clean.split("/")
        if len(parts) == 3 and parts[1] == "projects" and parts[2] in PROJECTS:
            return str(ROOT / f"{parts[2]}.html")
        local = super().translate_path(path)
        if not os.path.splitext(clean)[1] and not os.path.isdir(local) and os.path.isfile(local + ".html"):
            return local + ".html"
        return local

    def send_error(self, code, message=None, explain=None):
        """Missing pages show the site's own 404 page, as on Vercel."""
        page = ROOT / "404.html"
        if code == 404 and page.is_file():
            body = page.read_bytes()
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Expires", "0")
        self.send_header("Accept-Ranges", "bytes")
        super().end_headers()

    def send_head(self):
        """Serves "Range: bytes=start-end" requests with 206 Partial Content; everything else as usual."""
        match = re.fullmatch(r"bytes=(\d*)-(\d*)", self.headers.get("Range", "").strip())
        path = self.translate_path(self.path)
        if not match or os.path.isdir(path) or not os.path.isfile(path):
            self.range = None
            return super().send_head()
        size = os.path.getsize(path)
        first, last = match.groups()
        if first:
            start, end = int(first), min(int(last), size - 1) if last else size - 1
        else:  # "bytes=-N": the last N bytes
            start, end = max(size - int(last or 0), 0), size - 1
        if start >= size or start > end:
            self.send_response(416)
            self.send_header("Content-Range", f"bytes */{size}")
            self.end_headers()
            return None
        f = open(path, "rb")
        f.seek(start)
        self.range = end - start + 1
        self.send_response(206)
        self.send_header("Content-type", self.guess_type(path))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(self.range))
        self.end_headers()
        return f

    def copyfile(self, source, outputfile):
        if getattr(self, "range", None) is None:
            return super().copyfile(source, outputfile)
        remaining = self.range
        while remaining > 0:
            chunk = source.read(min(64 * 1024, remaining))
            if not chunk:
                break
            outputfile.write(chunk)
            remaining -= len(chunk)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    http.server.ThreadingHTTPServer(("", port), NoCacheHandler).serve_forever()
