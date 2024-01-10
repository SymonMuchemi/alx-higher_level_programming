#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxinteger(unittest.TestCase):
    """test the max_integer function

    Args:
        unittest (testcase): test cases
    """
    def test_max(self):
        """test with valid lists"""
        self.assertAlmostEqual(max_integer([10, 12, 0]), 12)
        self.assertAlmostEqual(max_integer([-10, -2, -25]), -2)
        self.assertAlmostEqual(max_integer([10]), 10)
        self.assertAlmostEqual(max_integer([]), None)
