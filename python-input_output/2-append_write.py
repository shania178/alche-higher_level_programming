#!/usr/bin/python3
"""Module for appending text to a file and returning the character count."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file.

    Returns the number of characters added.

    Args:
        filename (str): The path to the file to append to. Defaults to "".
        text (str): The text content to append to the file. Defaults to "".

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
