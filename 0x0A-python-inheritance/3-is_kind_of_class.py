#!/usr/bin/python3
"""
A function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object
    is an instance of a class that inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or its subclass,
        otherwise False.

    Example:
        class ParentClass:
            pass

        class ChildClass(ParentClass):
            pass

        obj1 = ParentClass()
        obj2 = ChildClass()
        obj3 = 42

        print(is_kind_of_class(obj1, ParentClass))  # Output: True
        print(is_kind_of_class(obj2, ParentClass))  # Output: True
        print(is_kind_of_class(obj3, ParentClass))  # Output: False
    """
    return isinstance(obj, a_class)
