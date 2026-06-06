#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """Return the addition of two integers.

    a and b must be integers or floats.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN or infinity WITHOUT importing math
    if a != a or a in (float('inf'), float('-inf')):
        raise TypeError("a must be an integer")

    if b != b or b in (float('inf'), float('-inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
