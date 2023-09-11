#!/usr/bin/python3
"""
A class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    BaseGeometry is a base class for geometric objects.
    It provides methods for area calculation and integer validation.

    Methods:
        area(self):
            This method is intended to be overridden by subclasses.
            It raises an Exception with the message "area() is not implemented"
            to indicate that subclasses should provide their own implementation
            for calculating the area.

        integer_validator(self, name, value):
            Validates that the given value is an integer and greater than 0.
            If value is not an integer, it raises a TypeError.
            If value is less than or equal to 0, it raises a ValueError.

    Example:
        class Rectangle(BaseGeometry):
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height

        rectangle = Rectangle(4, 5)
        print(rectangle.area())  # Output: 20
        rectangle.integer_validator("width", 4)
        rectangle.integer_validator("height", 5)
    """

    def area(self):
        """
        This method is intended to be overridden by subclasses.
        It raises an Exception with the message "area() is not implemented"
        to indicate that subclasses should provide their own implementation
        for calculating the area.

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is an integer and greater than 0.
        If value is not an integer, it raises a TypeError with the message
        "<name> must be an integer."
        If value is less than or equal to 0, it raises a ValueError with
        the message "<name> must be greater than 0."

        Args:
            name (str): The name of the value being validated
            (e.g., "width" or "height").
            value (int): The value to be validated.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
