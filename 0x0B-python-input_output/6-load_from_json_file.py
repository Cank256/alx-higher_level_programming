#!/usr/bin/python3
"""
A function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object represented by the JSON data in the file.
    """
    with open(filename, "r") as file:
        data = json.load(file)
    return data
