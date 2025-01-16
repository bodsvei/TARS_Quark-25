from http.server import HTTPServer, SimpleHTTPRequestHandler

host = "10.20.29.80"
port = 8000

class Server(SimpleHTTPRequestHandler):

    def doGet(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>TARS Quark'25</h1></body></html>","utf-8"))

server = HTTPServer((host, port), Server)
print("Server now running ...")

server.serve_forever()
server.server_close()

print("Server closed.")


