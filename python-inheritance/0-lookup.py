#!/usr/bin/python3
"""Module: lookup - Lists object attributes/methods."""


def lookup(obj):
    """Returns list of obj's attributes and methods.

    Args:
        obj (any): Object to inspect.

    Returns:
        list: List of attributes and methods.
    """
    return dir(obj)
