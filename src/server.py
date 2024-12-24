import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import markdown


class Server:
    """
    Object that manage both the request handler IndexPage who will serve the page and the HTTPServer.
    """

    index: str
    filename: str
    path: str

    class IndexPage(BaseHTTPRequestHandler):
        def do_GET(self):
            match self.path:
                case "/":
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html")
                    self.end_headers()
                    self.wfile.write(Server.index.encode("utf-8"))

                case "/content":
                    filepath = os.path.join(Server.path, Server.filename)

                    if os.path.exists(filepath):
                        self.send_response(200)
                        self.send_header("Content-Type", "text/plain")
                        self.end_headers()

                        with open(filepath, "r", encoding="utf-8") as file:
                            html_content = markdown.markdown(file.read())
                            self.wfile.write(html_content.encode("utf-8"))
                    else:
                        self.send_error(404, "Arquivo não encontrado")

                case "/raw-content":
                    filepath = os.path.join(Server.path, Server.filename)

                    if os.path.exists(filepath):
                        self.send_response(200)
                        self.send_header("Content-Type", "text/plain")
                        self.end_headers()

                        with open(filepath, "r", encoding="utf-8") as file:
                            markdown_content = file.read()
                            self.wfile.write(markdown_content.encode("utf-8"))
                    else:
                        self.send_error(404, "Arquivo não encontrado")

                case _:
                    self.send_error(404, "Endpoint não configurado")

    def __init__(self, index_page, path, filename):
        Server.index = index_page
        Server.path = path
        Server.filename = filename

    @staticmethod
    def serve():
        app = HTTPServer(("0.0.0.0", 8080), Server.IndexPage)
        app.serve_forever()
