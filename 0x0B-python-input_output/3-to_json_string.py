#!/usr/bin/python3
import json

"""
A function that returns the JSON representation
of an object (string)
"""


def to_json_string(my_obj):
    """
    Converts a Python object to its JSON representation as a string.

    Args:
        my_obj: The Python object to convert to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
