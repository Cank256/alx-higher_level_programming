#!/usr/bin/python3
"""
A class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
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
        It raises an Exception with the message "area() is not
        implemented" to indicate that subclasses should provide
        their own implementation for calculating the area.

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is an integer and
        greater than 0.
        If value is not an integer, it raises a TypeError with
        the message "<name> must be an integer."
        If value is less than or equal to 0, it raises a ValueError
        with the message "<name> must be greater than 0."

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
            Initializes a Rectangle instance with the specified width
            and height.
            Validates that width and height are positive integers.

        area(self):
            Calculates and returns the area of the rectangle.

        __str__(self):
            Returns a string representation of the rectangle in the format
            [Rectangle] <width>/<height>.

    Example:
        rectangle = Rectangle(4, 5)
        print(rectangle.area())  # Output: 20
        print(str(rectangle))  # Output: "[Rectangle] 4/5"
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the specified width
        and height.
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

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle in the format
        [Rectangle] <width>/<height>.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Square is a class that inherits from Rectangle.
    It represents a square with equal sides.

    Attributes:
        __size (int): The size of the square (private attribute).

    Methods:
        __init__(self, size):
            Initializes a Square instance with the specified size.
            Validates that size is a positive integer.

        area(self):
            Calculates and returns the area of the square.

        __str__(self):
            Returns a string representation of the square in the format
            [Square] <size>/<size>.

    Example:
        square = Square(5)
        print(square.area())  # Output: 25
        print(str(square))  # Output: "[Square] 5/5"
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the specified size.
        Validates that size is a positive integer.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square in the format
        [Square] <size>/<size>.

        Returns:
            str: A string representation of the square.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
