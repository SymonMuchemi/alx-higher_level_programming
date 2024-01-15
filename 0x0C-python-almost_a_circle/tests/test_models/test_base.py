#!/usr/bin/python3
"""tests the Base class"""
Base = __import__('../models/base').Base
import unittest


class TestBase(unittest.TestCase):
    def test_instance_id(self):
        obj1 = Base()
        obj2 = Base(24)
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 24)
