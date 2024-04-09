#!/usr/bin/python3
""" simple test"""
from models.base import Base
from unittest import TestCase

class TestBaseEx(TestCase):
    """Simple test case"""
    def test_private_attr(self):
        """check to see if the nb_object attr is private"""
        obj = Base()

        with self.assertRaises(AttributeError):
            obj.__nb_objects

