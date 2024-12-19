import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer

import markdown

parser = argparse.ArgumentParser(
    prog="vault",
    description="A command line program to open Markdown (.md) files into a local web editor.",
)

parser.add_argument("--file", type=str, help="the markdown file to open")

args = parser.parse_args()
filename = args.file
html_result = ""

with open(filename, "r") as file:
    html_result = markdown.markdown(file.read())


class Index(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(html_result.encode("utf-8"))


app = HTTPServer(("0.0.0.0", 8080), Index)
app.serve_forever()
