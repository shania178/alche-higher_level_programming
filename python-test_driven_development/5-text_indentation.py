#!/usr/bin/python3
"""Module that prints text with 2 new lines after '.', '?' and ':'"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'

    No space at beginning or end of printed lines.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n:
        # skip spaces at start of a line
        while i < n and text[i] == " ":
            i += 1

        while i < n:
            print(text[i], end="")

            if text[i] in ".?:":
                print("\n")
                i += 1

                # skip spaces after punctuation
                while i < n and text[i] == "":
                    i += 1

                break

            i += 1
