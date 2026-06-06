#!/usr/bin/python3
"""Module that prints text with 2 new lines after ., ? and :"""


def text_indentation(text):
    """Print a text with 2 new lines after '.', '?' and ':'.

    No space is printed at the beginning or end of each line.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")
            # skip spaces after punctuation
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1

        i += 1
