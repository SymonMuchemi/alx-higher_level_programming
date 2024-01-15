#!/usr/bin/python3
"""tests the Base class"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """class to test the models.base class

    Args:
        unittest (TestCase): test
    """
    def test_instance_id(self):
        """Test the user ID of the Base instances
        """
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        obj4 = Base(24)
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)
        self.assertEqual(obj4.id, 24)
