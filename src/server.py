import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Server:
    """
    Object that manage both the request handler IndexPage who will serve the page and the HTTPServer.
    """

    filename: str
    path: str

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/" or self.path == "/index":
                with open(
                    file="/home/deividsousan/Programação/vault/src/pages/index.html",
                    mode="r",
                    encoding="utf-8",
                ) as file:
                    index_page = file.read()

                    index_page = index_page.replace("[Document]", Server.filename)

                    index_page = index_page.replace("[Filename]", Server.filename)

                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(index_page.encode("utf-8"))
            elif self.path == "/get-content":
                filepath = os.path.join(Server.path, Server.filename)

                with open(filepath, "r", encoding="utf-8") as file:
                    file_content = file.read()

                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(file_content.encode("utf-8"))

        def do_POST(self):
            self.send_response(200)
            self.send_header("Content-Type", "plain/text")
            self.end_headers()

            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = post_data.decode("utf-8")

            filepath = os.path.join(Server.path, Server.filename)
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(post_data)

            self.wfile.write("Received.".encode("utf-8"))

    def __init__(self, path, filename):
        Server.path = path
        Server.filename = filename

    @staticmethod
    def serve():
        app = HTTPServer(("0.0.0.0", 8080), Server.RequestHandler)
        app.serve_forever()
