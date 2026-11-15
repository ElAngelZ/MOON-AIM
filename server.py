from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.request

class JPLHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/jpl?"):
            query = self.path.split("?", 1)[1]
            nasa_url = f"https://ssd.jpl.nasa.gov/api/horizons.api?{query}"
            try:
                # Petición directa a la NASA desde tu propia máquina
                req = urllib.request.urlopen(nasa_url, timeout=15)
                body = req.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(body)
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode())
        else:
            super().do_GET()

if __name__ == "__main__":
    server_address = ("localhost", 8000)
    print("🚀 Servidor local MOON AIM activo en http://localhost:8000")
    HTTPServer(server_address, JPLHandler).serve_forever()