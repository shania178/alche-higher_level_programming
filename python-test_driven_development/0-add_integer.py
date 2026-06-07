#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: First integer or float
        b: Second integer or float, defaults to 98

    Returns:
        The addition of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
