"""Local sink: receives POSTed text/base64 from the browser and writes it into trabalho/textos or entrada/artigos."""
import base64, os, sys, urllib.parse
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
ROOT = sys.argv[1]
class H(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Private-Network", "true")
    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()
    def do_POST(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        name = os.path.basename(q["name"][0]); kind = q.get("kind", ["txt"])[0]
        body = self.rfile.read(int(self.headers["Content-Length"]))
        if kind == "b64":
            path = os.path.join(ROOT, "entrada", "artigos", name); data = base64.b64decode(body)
        else:
            path = os.path.join(ROOT, "trabalho", "textos", name); data = body
        open(path, "wb").write(data)
        self.send_response(200); self._cors(); self.end_headers(); self.wfile.write(f"saved {len(data)}".encode())
    def log_message(self, *a): pass
ThreadingHTTPServer(("127.0.0.1", 8765), H).serve_forever()
