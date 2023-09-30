#!/usr/bin/python3
import unittest
from max_integer import max_integer
"""
A max integer test
"""

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

        # Test with a list containing both positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

        # Test with a list containing duplicate values
        self.assertEqual(max_integer([1, 2, 2, 1, 5]), 5)

        # Test with an empty list, should return None
        self.assertIsNone(max_integer([]))

        # Test with a list of one element, should return that element
        self.assertEqual(max_integer([42]), 42)

        # Test with a large list
        self.assertEqual(max_integer(list(range(1, 10001))), 10000)

if __name__ == '__main__':
    unittest.main()
