#!/usr/bin/python3
"""
A function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the specified
class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class,
        otherwise False.

    Example:
        class Grandparent:
            pass

        class Parent(Grandparent):
            pass

        class Child(Parent):
            pass

        obj1 = Parent()
        obj2 = Child()
        obj3 = 42

        print(inherits_from(obj1, Grandparent))  # Output: True
        print(inherits_from(obj2, Grandparent))  # Output: True
        print(inherits_from(obj3, Grandparent))  # Output: False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
