#!/usr/bin/python3
"""
A python class to represent a rectangle
"""


# class Rectangle:
#     """A class that defines a rectangle."""

#     def __init__(self, width=0, height=0):
#         """
#         Initialize a new Rectangle instance.

#         Args:
#             width (int, optional): The width of the rectangle (default is 0).
#             height (int, optional): The height of the rectangle (default is 0).
#         """
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         """
#         Get the width of the rectangle.

#         Returns:
#             int: The width of the rectangle.
#         """
#         return self._width

#     @width.setter
#     def width(self, value):
#         """
#         Set the width of the rectangle.

#         Args:
#             value (int): The new width value.

#         Raises:
#             TypeError: If the value is not an integer.
#             ValueError: If the value is less than 0.
#         """
#         if not isinstance(value, int):
#             raise TypeError("width must be an integer")
#         if value < 0:
#             raise ValueError("width must be >= 0")
#         self._width = value

#     @property
#     def height(self):
#         """
#         Get the height of the rectangle.

#         Returns:
#             int: The height of the rectangle.
#         """
#         return self._height

#     @height.setter
#     def height(self, value):
#         """
#         Set the height of the rectangle.

#         Args:
#             value (int): The new height value.

#         Raises:
#             TypeError: If the value is not an integer.
#             ValueError: If the value is less than 0.
#         """
#         if not isinstance(value, int):
#             raise TypeError("height must be an integer")
#         if value < 0:
#             raise ValueError("height must be >= 0")
#         self._height = value

class Rectangle:
    """A class that defines a rectangle."""

    def __init__(self, height=0, width=0):
        """
        Initialize a new Rectangle instance.

        Args:
            height (int, optional): The height of the rectangle (default is 0).
            width (int, optional): The width of the rectangle (default is 0).
        """
        self._height = height
        self._width = width

        if not isinstance(self._height, int):
            raise TypeError("height must be an integer")
        if self._height < 0:
            raise ValueError("height must be >= 0")
        
        if not isinstance(self._width, int):
            raise TypeError("width must be an integer")
        if self._width < 0:
            raise ValueError("width must be >= 0")
        
        def height(self):
            """
            Get the height of the rectangle.

            Returns:
                int: The height of the rectangle.
            """
            return self._height
        
        def width(self):
            """
            Get the width of the rectangle.

            Returns:
                int: The width of the rectangle.
            """
            return self._width
