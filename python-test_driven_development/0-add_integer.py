#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """Return the sum of two integers or floats cast to integers."""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # Handle NaN (NaN is the only value that is not equal to itself)
    if a != a:
        raise ValueError("a must be an integer")

    if b != b:
        raise ValueError("b must be an integer")

    # Handle infinity (ALX checks overflow case)
    if a in (float('inf'), float('-inf')):
        raise OverflowError("a must be an integer")

    if b in (float('inf'), float('-inf')):
        raise OverflowError("b must be an integer")

    return int(a) + int(b)
