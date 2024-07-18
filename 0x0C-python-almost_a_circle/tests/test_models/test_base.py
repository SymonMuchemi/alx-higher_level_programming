#!/usr/bin/python3
"""Test the base model"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test the base model

    Args:
        unittest (TestCase): test cases
    """
    @classmethod
    def setUpClass(cls):
        cls.baseNoId = Base()
        cls.base1 = Base()
        cls.base2 = Base()
        cls.base_with_id = Base(89)

    def test_base_attributes(self):
        self.assertFalse(hasattr(TestBase.base_with_id, '__nb_objects'))
        self.assertTrue(hasattr(TestBase.base_with_id, 'id'))

    def test_id_exists(self):
        self.assertIsNotNone(TestBase.base_with_id.id)
        self.assertIsNotNone(TestBase.baseNoId.id)

    def test_id_as_instantiation(self):
        self.assertEqual(TestBase.base_with_id.id, 89)

    def test_id_increment_by_1(self):
        diff = TestBase.base2.id - TestBase.base1.id
        self.assertEqual(1, diff)


if __name__ == "__main__":
    unittest.main()
