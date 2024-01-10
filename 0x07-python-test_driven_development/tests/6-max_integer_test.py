#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test the max_integer function

    Args:
        unittest (testcase): test cases
    """
    def test_max(self):
        """test with valid lists"""
        self.assertAlmostEqual(max_integer([10, 12, 0]), 12)
        self.assertEqual(max_integer([-3]), -3)
        self.assertAlmostEqual(max_integer([-10, -2, -25]), -2)
        self.assertAlmostEqual(max_integer([10]), 10)
        self.assertAlmostEqual(max_integer([]), None)

    def test_type_error(self):
        """ type_errors """
        self.assertRaises(TypeError, max_integer, ["h", 1])
        self.assertRaises(TypeError, max_integer, [2, [2, 1]])
