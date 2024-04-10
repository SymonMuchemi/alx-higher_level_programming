#!/usr/bin/python3
"""tests the Base class"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """class to test the models.base class

    Args:
        unittest (TestCase): test
    """
    def test_private_attribute(self):
        """Checks if the nb_objects att is private"""
        obj = Base()
        
        # Confirm private attribute is not accessible
        with self.assertRaises(AttributeError): obj.__nb_objects
