#!/usr/bin/python3
"""
A rectangle Module

"""


class Rectangle:
    """A class that defines a rectangle."""

    number_of_instances = 0  # Class attribute to keep track of instances
    print_symbol = "#"      # Class attribute for string representation symbol

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the instance count

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

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

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

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """
        Return a string representation of the rectangle using print_symbol.

        Returns:
            str: A string representation of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""
        else:
            return "\n".join(
                [str(self.print_symbol) * self._width] * self._height
            )

    def __repr__(self):
        """
        Return a string representation of the rectangle for recreation.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """
        Print a deletion message when the Rectangle instance is deleted
        and decrement the instance count.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
