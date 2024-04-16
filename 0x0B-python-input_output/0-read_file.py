#!/usr/bin/python3
"""This Module defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF-8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
