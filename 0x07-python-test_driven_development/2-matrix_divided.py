#!/usr/bin/python3
"""
A module to divide a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
    matrix (list of lists): The matrix to be divided. Each element must be an integer or float.
    div (int or float): The divisor to divide all matrix elements by.

    Returns:
    list of lists: A new matrix with the elements divided by the divisor, rounded to 2 decimal places.

    Raises:
    TypeError: If the input matrix is not a list of lists containing integers or floats,
               if the rows of the matrix are of different sizes, or if div is not a number.
    ZeroDivisionError: If div is equal to 0.

    Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    divisor = 2
    result = matrix_divided(matrix, divisor)
    """
    
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create a new matrix to store the divided values
    result_matrix = []
    
    # Divide each element of the matrix by div and round to 2 decimal places
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        result_matrix.append(new_row)
    
    return result_matrix
