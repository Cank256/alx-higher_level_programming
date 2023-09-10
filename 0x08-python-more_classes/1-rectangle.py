#!/usr/bin/python3
"""
A python class to represent a rectangle
"""


class Rectangle:
    """A class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).

        Raises:
            TypeError: If the value of height or width is not an integer.
            ValueError: If the value of height or width is less than 0.
        """
        self._width = width
        self._height = height

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if self._height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if self._width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.
        """
        self._height = value

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.
        """
        self._width = value
