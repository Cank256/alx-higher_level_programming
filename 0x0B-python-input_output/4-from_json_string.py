#!/usr/bin/python3
import json

"""
A function that returns an object (Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """
    Parses a JSON string and returns the corresponding Python object.

    Args:
        my_str (str): The JSON string to parse.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
