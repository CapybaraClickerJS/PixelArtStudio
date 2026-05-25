# dev_server.py
import http.server
import socketserver
import os
import time
import threading

PORT = 5173
ROOT = os.path.join(os.path.dirname(__file__), "src")
os.chdir(ROOT)

clients = []

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        if self.path == "/__live_reload":
            self.send_response(200)
            self.end_headers()
            clients.append(self.wfile)
            return
        return super().do_GET()

def watcher():
    last = {}

    while True:
        changed = False
        for root, _, files in os.walk(ROOT):
            for f in files:
                path = os.path.join(root, f)
                m = os.path.getmtime(path)
                if path not in last or last[path] != m:
                    last[path] = m
                    changed = True

        if changed:
            for c in clients:
                try:
                    c.write(b"reload")
                except:
                    pass
            clients.clear()

        time.sleep(1)

threading.Thread(target=watcher, daemon=True).start()

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"🔥 Dev server: http://localhost:{PORT}")
    httpd.serve_forever()