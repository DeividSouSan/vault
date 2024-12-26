import argparse
import os

from server import Server


def main() -> None:
    """
    Configure the argparser feature, reads the arguments and opens the server.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(
        prog="vault",
        description="A command line program to open Markdown (.md) files into a local web editor.",
    )

    parser.add_argument("--file", type=str, help="the markdown file to open")

    # Catch the given argument
    args = vars(parser.parse_args())
    filename = args["file"]

    # Open the HTTP Server
    print("Server: http://localhost:8080/")
    server = Server(os.getcwd(), filename)
    server.serve()


if __name__ == "__main__":
    main()
