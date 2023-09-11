#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry
(7-base_geometry.py).
"""


class BaseGeometry:
    """
    BaseGeometry is a base class for geometric objects.
    It provides methods for area calculation and integer validation.

    Methods:
        area(self):
            This method is intended to be overridden by subclasses.
            It raises an Exception with the message "area() is not
            implemented" to indicate that subclasses should provide
            their own implementation for calculating the area.

        integer_validator(self, name, value):
            Validates that the given value is an integer and
            greater than 0.
            If value is not an integer, it raises a TypeError.
            If value is less than or equal to 0, it raises a
            ValueError.

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
        It raises an Exception with the message "area() is not
        implemented" to indicate that subclasses should provide
        their own implementation for calculating the area.

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is an integer
        and greater than 0.
        If value is not an integer, it raises a TypeError
        with the message "<name> must be an integer."
        If value is less than or equal to 0, it raises a
        ValueError with the message "<name> must be greater than 0."

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


class Rectangle(BaseGeometry):
    """
    Rectangle is a class that inherits from BaseGeometry.
    It represents a rectangle with width and height.

    Attributes:
        __width (int): The width of the rectangle (private attribute).
        __height (int): The height of the rectangle (private attribute).

    Methods:
        __init__(self, width, height):
            Initializes a Rectangle instance with the specified
            width and height.
            Validates that width and height are positive integers.

    Example:
        rectangle = Rectangle(4, 5)
        print(rectangle.area())  # Output: 20
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the specified width and height.
        Validates that width and height are positive integers.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Returns:
            None
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
