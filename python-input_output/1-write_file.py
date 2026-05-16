#!/usr/bin/python3
"""Module for writing text to a file and returning the character count."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the number of characters written.

    Args:
        filename (str): The path to the file to write to. Defaults to "".
        text (str): The text content to write to the file. Defaults to "".

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
