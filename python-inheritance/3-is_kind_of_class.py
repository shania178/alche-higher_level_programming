#!/usr/bin/python3
"""Defines a function that checks if an object
is an instance of a class or inherited class.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class
    or inherits from it, otherwise False.
    """
    return isinstance(obj, a_class)
