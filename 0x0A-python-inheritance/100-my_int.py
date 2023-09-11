#!/usr/bin/python3
"""
A class MyInt that inherits from int
"""


class MyInt(int):
    """
    MyInt is a subclass of int with inverted equality operators
    (== and !=).

    Methods:
        __eq__(self, other):
            Overrides the equality operator (==) to invert its behavior.

        __ne__(self, other):
            Overrides the inequality operator (!=) to invert its behavior.

    Example:
        num1 = MyInt(5)
        num2 = MyInt(5)
        num3 = MyInt(10)

        print(num1 == num2)  # Output: False
        print(num1 != num2)  # Output: True
        print(num1 == num3)  # Output: True
        print(num1 != num3)  # Output: False
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==) to invert its behavior.

        Args:
            other (int): The other integer to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to invert its behavior.

        Args:
            other (int): The other integer to compare.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
