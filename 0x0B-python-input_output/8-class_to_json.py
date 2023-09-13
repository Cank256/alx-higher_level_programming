#!/usr/bin/python3
"""
A function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an objec
"""


def class_to_json(obj):
    """
    Converts an object with serializable attributes to a
    dictionary for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object for
        JSON serialization.
    """
    # Initialize an empty dictionary to store the JSON representation
    json_dict = {}

    # Get all attributes of the object
    attributes = dir(obj)

    for attribute_name in attributes:
        # Skip private attributes (those starting with an underscore)
        if attribute_name.startswith("_"):
            continue

        # Get the attribute value
        attribute_value = getattr(obj, attribute_name)

        # Check if the attribute is serializable
        # (list, dictionary, string, integer, or boolean)
        if isinstance(attribute_value, (list, dict, str, int, bool)):
            json_dict[attribute_name] = attribute_value

    return json_dict
