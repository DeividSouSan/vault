import argparse

parser = argparse.ArgumentParser(
    prog="vault",
    description="A command line program to open Markdown (.md) files into a local web editor.",
)

parser.add_argument("--file", type=str, help="the markdown file to open")

args = parser.parse_args()
filename = args.file

with open(filename, "r") as file:
    print(file.read())
