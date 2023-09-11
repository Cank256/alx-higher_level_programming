#!/usr/bin/python3
"""
A class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """
    BaseGeometry is a base class for geometric objects.
    It provides a placeholder method for calculating the area.

    Methods:
        area(self):
            This method is intended to be overridden by subclasses.
            It raises an Exception with the message
            "area() is not implemented" to indicate that subclasses should
            provide their own implementation
            for calculating the area.

    Example:
        class Rectangle(BaseGeometry):
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height

        rectangle = Rectangle(4, 5)
        print(rectangle.area())  # Output: 20
    """

    def area(self):
        """
        This method is intended to be overridden by subclasses.
        It raises an Exception with the message "area() is not implemented"
        to indicate that subclasses should provide their own implementation
        for calculating the area.

        Returns:
            None

        Example:
            class Rectangle(BaseGeometry):
                def __init__(self, width, height):
                    self.width = width
                    self.height = height

                def area(self):
                    return self.width * self.height

            rectangle = Rectangle(4, 5)
            print(rectangle.area())  # Output: 20
        """
        raise Exception("area() is not implemented")
