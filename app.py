from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body>Hello World from Docker!</body></html>", "utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), HelloHandler)
    print("Server started at http://localhost:8080")
    server.serve_forever()
