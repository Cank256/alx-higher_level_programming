#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        mid_value = list_of_integers[mid]
        next_value = list_of_integers[mid + 1]

        if mid_value < next_value:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
