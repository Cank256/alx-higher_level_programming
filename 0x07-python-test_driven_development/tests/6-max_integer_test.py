#!/usr/bin/python3
import unittest
"""
A max integer test
"""


def max_integer(lst=[]):
    # Your implementation of the max_integer function goes here
    pass


class TestMaxInteger(unittest.TestCase):

    def test_max_integer_positive_values(self):
        # Test when the list contains positive integers
        result = max_integer([1, 3, 5, 7, 9])
        self.assertEqual(result, 9)

    def test_max_integer_negative_values(self):
        # Test when the list contains negative integers
        result = max_integer([-1, -3, -5, -7, -9])
        self.assertEqual(result, -1)

    def test_max_integer_mixed_values(self):
        # Test when the list contains mixed positive and negative integers
        result = max_integer([-2, 4, -6, 8, -10])
        self.assertEqual(result, 8)

    def test_max_integer_single_value(self):
        # Test when the list contains a single value
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_max_integer_empty_list(self):
        # Test when the list is empty, should return None
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_float_values(self):
        # Test when the list contains floating-point numbers
        result = max_integer([1.5, 2.7, 3.9])
        self.assertEqual(result, 3.9)

    def test_max_integer_mixed_numbers(self):
        # Test when the list contains mixed integers and floating-point numbers
        result = max_integer([1, 2.5, 3, 4.7, 5])
        self.assertEqual(result, 5)

    def test_max_integer_with_duplicates(self):
        # Test when the list contains duplicate values
        result = max_integer([4, 7, 4, 9, 7, 7])
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
