#!/usr/bin/python3
"""Module that provides a text indentation function."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' or ':' character.

    Args:
        text (str): The text to be printed with indentation.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
