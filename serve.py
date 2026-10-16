"""Local preview that serves the site the way Vercel does (see vercel.json):

    /about            -> about.html            /about.html -> redirects to /about
    /projects/atlas   -> atlas.html            /atlas.html -> redirects to /projects/atlas
    anything missing  -> 404.html

Run it from this folder, then open http://localhost:8000

    python3 serve.py
"""

import http.server
import re
from functools import partial
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).parent
PROJECTS = "atlas|denglish|elev8|rise|stuartfox"


class Handler(http.server.SimpleHTTPRequestHandler):
    def redirect(self, location):
        self.send_response(308)
        self.send_header("Location", location)
        self.end_headers()

    def route(self):
        parts = urlsplit(self.path)
        path, query = parts.path, ("?" + parts.query if parts.query else "")
        if m := re.fullmatch(rf"/({PROJECTS})(\.html)?", path):
            return self.redirect(f"/projects/{m.group(1)}{query}")
        if path == "/index.html":
            return self.redirect("/" + query)
        if path.endswith(".html") and (ROOT / path.lstrip("/")).is_file():
            return self.redirect(path[: -len(".html")] + query)
        if m := re.fullmatch(rf"/projects/({PROJECTS})", path):
            self.path = f"/{m.group(1)}.html{query}"
        elif path != "/" and "." not in path.rsplit("/", 1)[-1] and (ROOT / f"{path.lstrip('/')}.html").is_file():
            self.path = f"{path}.html{query}"
        return True

    def do_GET(self):
        if self.route() is True:
            super().do_GET()

    def do_HEAD(self):
        if self.route() is True:
            super().do_HEAD()

    def send_error(self, code, message=None, explain=None):
        page = ROOT / "404.html"
        if code == 404 and page.exists():
            body = page.read_bytes()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)


if __name__ == "__main__":
    print("Previewing at http://localhost:8000")
    http.server.ThreadingHTTPServer(("127.0.0.1", 8000), partial(Handler, directory=str(ROOT))).serve_forever()
