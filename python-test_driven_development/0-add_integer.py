#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """Return the sum of two integers.

    Floats are cast to integers.
    Raises TypeError if inputs are not int or float.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
