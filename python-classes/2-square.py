#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a square with size validation."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
