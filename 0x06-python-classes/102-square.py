#!/usr/bin/python3
"""
A python square class
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (float or int): The size of each side of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (float or int, optional): The size of each side of the square.
                                        Defaults to 0.
        Raises:
            TypeError: If the provided size is not a number (float or integer).
            ValueError: If the provided size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The size of each side of the square.

        Raises:
            TypeError: If the provided size is not a number (float or integer).
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Implements the equality comparator.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Implements the inequality comparator.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Implements the less-than comparator.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less than the other area,
            False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Implements the less-than-or-equal-to comparator.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less than or equal to
            the other area, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Implements the greater-than comparator.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater than the other area,
            False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Implements the greater-than-or-equal-to comparator.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater than or equal to the
            other area, False otherwise.
        """
        return self.area() >= other.area()
