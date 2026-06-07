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
    # Check type first (before any operations)
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    # Check for NaN (NaN is not equal to itself) - must be after type check
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    # Check for infinity
    if a == float('inf') or a == -float('inf'):
        raise TypeError("a must be an integer")
    if b == float('inf') or b == -float('inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
