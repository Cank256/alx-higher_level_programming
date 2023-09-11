#!/usr/bin/python3
def lookup(obj):
    """
    Use the dir() function to get a list
    of attributes and methods of the object
    """
    attributes_and_methods = dir(obj)

    """
    Filter out attributes and methods that
    start with '__' (usually special methods)
    """
    filtered_attributes_and_methods = [
        item for item in attributes_and_methods if not item.startswith('__')
    ]

    return filtered_attributes_and_methods
