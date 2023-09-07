#!/usr/bin/python3
"""
A module that prints a square
"""


def print_square(size):
    """
    Prints a square of '#' characters with the specified size.

    Args:
    size (int): The size of the square.

    Returns:
    None

    Raises:
    TypeError: If size is not an integer or if size is a float less than 0.
    ValueError: If size is less than 0.

    Example:
    print_square(3)
    Output:
    ###
    ###
    ###
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is a float and less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
