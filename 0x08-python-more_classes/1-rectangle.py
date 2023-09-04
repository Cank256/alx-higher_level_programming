#!/usr/bin/python3
"""
An empty python class to represent a rectangle
"""


class Rectangle():
    """
    This class represents a rectangle.

    Attributes:
        __width (int): The size of each side of the rectangle.
        __height (int): The height of each side of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Square instance.

        Args:
            width (int): The width of each side of the rectangle.
            height (int): The height of each side of the rectangle.
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
