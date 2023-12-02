#!/usr/bin/python3
"""
Module for dividing all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix.

    Args:
        matrix (list): List of lists of integers or floats.
        div (int/float): The number to divide the matrix by.

    Returns:
        list: A new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists or div is not a number.
        ValueError: If matrix is empty or div is zero.

    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists of integers/floats")
    if not matrix or any(not row for row in matrix):
        raise ValueError("matrix can't be empty")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
