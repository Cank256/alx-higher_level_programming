#!/usr/bin/python3
"""
A function def pascal_triangle(n): that returns alist of
lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: Pascal's triangle as a list of
        lists of integers.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # The first element of each row is always 1
        if i > 0:
            # Generate the elements in the current row
            # based on the previous row
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle
