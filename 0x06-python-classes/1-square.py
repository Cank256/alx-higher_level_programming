#!/usr/bin/python3
"""
A python class to represent a square
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (float): The size of each side of the square.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (float): The size of each side of the square.
        """
        self.__size = size
