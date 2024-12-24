import argparse
import logging
import os

import markdown

from server import Server


def main():
    """
    Basic configurations of the app:
    - Logging
    - Argument Parser
    - Markdown to HTML translation
    - Serving the server
    """
    # Configurando o log
    logging.basicConfig(filename="myapp.log", level=logging.INFO)

    # Configurando o argparser
    parser = argparse.ArgumentParser(
        prog="vault",
        description="A command line program to open Markdown (.md) files into a local web editor.",
    )

    parser.add_argument("--file", type=str, help="the markdown file to open")

    # Tentando capturar o valor passado como parametro
    try:
        args = vars(parser.parse_args())
        filename = args["file"]
    except:
        logging.info("Couldn't get arguments.")
        quit()

    # Abrindo o servidor e servindo index.html
    with open(
        "/home/deividsousan/Programação/vault/src/pages/index.html",
        "r",
        encoding="utf-8",
    ) as file:
        index_page = file.read()

    index_page = index_page.replace(
        "<title>Document</title>", f"<title>{filename}</title>"
    )

    print("Servidor rodando na porta: http://localhost:8080/")
    server = Server(index_page, os.getcwd(), filename)
    print(os.path.join(os.getcwd(), filename))
    server.serve()


if __name__ == "__main__":
    main()
