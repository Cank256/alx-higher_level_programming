#!/usr/bin/python3
"""
A function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to save to the file.
        filename (str): The name of the file to write the
        JSON representation to.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
