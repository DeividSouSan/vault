from http.server import BaseHTTPRequestHandler, HTTPServer


class Server:
    """
    Object that manage both the request handler IndexPage who will serve the page and the HTTPServer.
    """

    content: str

    class IndexPage(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(Server.content.encode("utf-8"))

    def __init__(self, content):
        Server.content = content

    @staticmethod
    def serve():
        app = HTTPServer(("0.0.0.0", 8080), Server.IndexPage)
        app.serve_forever()
