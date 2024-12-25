import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import markdown


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
                    "/home/deividsousan/Programação/vault/src/pages/index.html",
                    "r",
                    encoding="utf-8",
                ) as file:
                    index_page = file.read()

                    index_page = index_page.replace(
                        "[Document]",
                        Server.filename,
                    )

                    index_page = index_page.replace(
                        "[Filename]",
                        Server.filename,
                    )

                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(index_page.encode("utf-8"))

            elif self.path == "/html-content":
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

            elif self.path == "/md-content":
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

            else:
                self.send_error(404, "Endpoint não configurado")

    def __init__(self, path, filename):
        Server.path = path
        Server.filename = filename

    @staticmethod
    def serve():
        app = HTTPServer(("0.0.0.0", 8080), Server.RequestHandler)
        app.serve_forever()
