#!/usr/bin/python3
"""
An empty python class to represent a rectangle
"""


class Rectangle():
    """
    This class represents a rectangle.

    Attributes:
        __width (float): The size of each side of the rectangle.
        __height (float): The height of each side of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a new Square instance.

        Args:
            width (float): The width of each side of the rectangle.
            height (float): The height of each side of the rectangle.
        """
        self.__width = width
        self.__height = height
