import argparse
import logging

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
    logging.basicConfig(filename="myapp.log", level=logging.INFO)

    parser = argparse.ArgumentParser(
        prog="vault",
        description="A command line program to open Markdown (.md) files into a local web editor.",
    )

    parser.add_argument("--file", type=str, help="the markdown file to open")

    try:
        args = vars(parser.parse_args())
        filename = args["file"]
    except:
        logging.info("Couldn't get arguments.")
        quit()

    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            markdownn_text = file.read()
            html_translated_md = markdown.markdown(markdownn_text)

        server = Server(html_translated_md)
        server.serve()

    else:
        logging.info("Argument --file not given.")
        quit()


if __name__ == "__main__":
    main()
