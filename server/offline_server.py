import http.server
import socketserver
import os
import webbrowser
import time
from pathlib import Path

# ==============================
# ⚙️ CONFIG
# ==============================
PORT = 8080
AUTO_OPEN_BROWSER = True
ENABLE_LOGS = True

# ==============================
# 📁 ROOT FIX (MUITO IMPORTANTE)
# ==============================
BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

if ENABLE_LOGS:
    print("\n🚀 PixelArt Studio Server (Vercel Local Mode)")
    print(f"📁 Root: {BASE_DIR}")
    print(f"🌐 http://localhost:{PORT}\n")

# ==============================
# 🎯 HANDLER MELHORADO
# ==============================
class CustomHandler(http.server.SimpleHTTPRequestHandler):

    def log_message(self, format, *args):
        if ENABLE_LOGS:
            print(f"🟢 {self.client_address[0]} -> {format % args}")

    def end_headers(self):
        # 🔥 cache desligado (modo dev tipo Vercel)
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

        # favicon fix extra (evita bug chato de alguns browsers)
        self.send_header("Access-Control-Allow-Origin", "*")

        super().end_headers()

    def do_GET(self):
        # 🔥 auto fallback tipo Vercel (SPA style)
        if self.path != "/" and not os.path.exists(BASE_DIR / self.path.lstrip("/")):
            if self.path.startswith("/assets") or "." in self.path:
                return super().do_GET()

            self.path = "/index.html"

        return super().do_GET()


# ==============================
# 🚀 START SERVER
# ==============================
Handler = CustomHandler

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:

    if AUTO_OPEN_BROWSER:
        time.sleep(0.5)
        webbrowser.open(f"http://localhost:{PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server parado com sucesso")