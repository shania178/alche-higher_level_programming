#!/usr/bin/python3
"""Module for converting an object to its JSON string representation."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object.

    Args:
        my_obj: The object to serialize to JSON.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
