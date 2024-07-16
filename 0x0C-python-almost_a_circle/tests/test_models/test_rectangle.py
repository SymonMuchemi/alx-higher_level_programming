#!/usr/bin/python3
"""tests for the Rectangle"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectagle(unittest.TestCase):
    """ """
    rect = Rectangle(21, 12, 5, 4)

    def test_rectangle_parent_class(self):
        self.assertIsInstance(TestRectagle.rect, Base)

    def test_rectangle_attributes(self):
        self.assertFalse(hasattr(TestRectagle.rect, '__width'))
        self.assertFalse(hasattr(TestRectagle.rect, '__height'))
        self.assertFalse(hasattr(TestRectagle.rect, '__x'))
        self.assertFalse(hasattr(TestRectagle.rect, '__y'))

    def test_width_getter(self):
        self.assertEqual(TestRectagle.rect.width, 21)

    def test_height_getter(self):
        self.assertEqual(TestRectagle.rect.height, 12)

    def test_x_getter(self):
        self.assertEqual(TestRectagle.rect.x, 5)

    def test_y_getter(self):
        self.assertEqual(TestRectagle.rect.y, 4)

    def test_height_setter(self):
        TestRectagle.rect.height = 32

        self.assertEqual(TestRectagle.rect.height, 32)

    def test_width_setter(self):
        TestRectagle.rect.width = 32

        self.assertEqual(TestRectagle.rect.width, 32)

    def test_x_setter(self):
        TestRectagle.rect.x = 0

        self.assertEqual(TestRectagle.rect.x, 0)

    def test_y_setter(self):
        TestRectagle.rect.y = 10

        self.assertEqual(TestRectagle.rect.y, 10)

    def test_width_setter_raises_Type_error(self):
        with self.assertRaises(TypeError) as context:
            TestRectagle.rect.width = "Mellon"

        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            TestRectagle.rect.width = -90

        self.assertEqual(str(context.exception), "width must be > 0")

    def test_height_setter_raises_Type_error(self):
        with self.assertRaises(TypeError) as context:
            TestRectagle.rect.height = "Mellon"

        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            TestRectagle.rect.height = -90

        self.assertEqual(str(context.exception), "height must be > 0")

    def test_x_setter_raises_Type_error(self):
        with self.assertRaises(TypeError) as context:
            TestRectagle.rect.x = "Mellon"

        self.assertEqual(str(context.exception), "x must be an integer")

    def test_y_setter_raises_Type_error(self):
        with self.assertRaises(TypeError) as context:
            TestRectagle.rect.y = "Mellon"

        self.assertEqual(str(context.exception), "y must be an integer")

    def test_x_setter_does_not_raise_value_error(self):
        try:
            TestRectagle.rect.x = -10
        except ValueError:
            self.fail("x.setter raises a value error")

    def test_y_setter_does_not_raise_value_error(self):
        try:
            TestRectagle.rect.y = -98
        except ValueError:
            self.fail("y.setter raises a value error")
