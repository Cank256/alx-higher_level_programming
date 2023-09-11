#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class, otherwise False.

    Example:
        class MyClass:
            pass

        obj1 = MyClass()
        obj2 = 42

        print(is_same_class(obj1, MyClass))  # Output: True
        print(is_same_class(obj2, MyClass))  # Output: False
    """
    return type(obj) is a_class
