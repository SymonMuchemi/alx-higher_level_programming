#!/usr/bin/python3
"""Test the base model"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test the base model

    Args:
        unittest (TestCase): test cases
    """
    baseNoId = Base()
    base_with_id = Base(89)

    def test_base_attributes(self):
        self.assertFalse(hasattr(TestBase.base_with_id, '__nb_objects'))
        self.assertTrue(hasattr(TestBase.base_with_id, 'id'))

    def test_id(self):
        self.assertIsNotNone(TestBase.base_with_id.id)
        self.assertIsNotNone(TestBase.baseNoId.id)
        self.assertEqual(TestBase.base_with_id.id, 89)


if __name__ == "__main__":
    unittest.main()
