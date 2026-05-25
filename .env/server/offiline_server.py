from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

PORT = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

os.chdir("../app/src/main/assets")

with TCPServer(("0.0.0.0", PORT), MyHandler) as httpd:
    print(f"PixelArt Studio Offline Server rodando em:")
    print(f"http://localhost:{PORT}")
    print(f"http://127.0.0.1:{PORT}")
    httpd.serve_forever()