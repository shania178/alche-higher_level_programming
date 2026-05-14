#!/usr/bin/python3
"""This module reads a UTF-8 file and prints its content to stdout."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
