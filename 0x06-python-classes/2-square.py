#!/usr/bin/python3
"""
A python class to represent a square
"""
class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of each side of the square.
    """
    
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of each side of the square. Defaults to 0.
        
        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError('Size must be an integer')
        if size < 0:
            raise ValueError('Size must be greater than or equal to zero')
        self.__size = size
