#!/usr/bin/python3
"""
Module for adding integers.
"""


def add_integer(a, b=98):
    """
    Function to add two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer (default is 98).

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    Example:
        >>> add_integer(1, 2)
        3
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
