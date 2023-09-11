#!/usr/bin/python3
"""
A function that adds a new attribute to an object if
it’s possible
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute should be added.
        attr_name (str): The name of the new attribute.
        attr_value: The value of the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes,
        a TypeError is raised with the message
        "can't add new attribute."

    Example:
        class ExampleClass:
            pass

        obj = ExampleClass()
        add_attribute(obj, "new_attr", 42)
        # This will add a new attribute "new_attr" to obj
    """
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__')
                                    and attr_name in type(obj).__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
