#!/usr/bin/python3
"""Module that prints text with 2 new lines after '.', '?' and ':'"""


def text_indentation(text):
    """Print text with formatting rules for punctuation."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n:
        print(text[i], end="")

        if text[i] in ".?:":
            print()  # ONLY ONE newline, not forced blank line

            # skip spaces after punctuation
            i += 1
            while i < n and text[i] == " ":
                i += 1

            continue

        i += 1
