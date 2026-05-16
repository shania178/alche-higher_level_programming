#!/usr/bin/python3
"""Module for saving an object to a file using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation.

    Args:
        my_obj: The object to serialize and save to the file.
        filename (str): The path to the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
