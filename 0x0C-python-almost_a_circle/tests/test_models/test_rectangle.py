#!/usr/bin/python3
"""tests for the Rectangle"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectagle(unittest.TestCase):
    """ """
    rect = Rectangle(21, 12, 5, 4)
    rect_with_id = Rectangle(21, 12, 5, 4, 89)
    smallRect = Rectangle(2, 3, 2, 5)

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
        TestRectagle.rect.x = 10

        self.assertEqual(TestRectagle.rect.x, 10)

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

    def test_x_raises_value_error(self):
        with self.assertRaises(ValueError) as cntxtNegative:
            TestRectagle.rect.x = -6

        self.assertEqual(str(cntxtNegative.exception), "x must be >= 0")

        try:
            TestRectagle.rect.x = 0
        except ValueError:
            self.fail("x.setter raises ValueError on x = 0")

    def test_y_raises_value_error(self):
        with self.assertRaises(ValueError) as cntxtNegative:
            TestRectagle.rect.y = -6

        self.assertEqual(str(cntxtNegative.exception), "y must be >= 0")

        try:
            TestRectagle.rect.y = 0
        except ValueError:
            self.fail("y.setter raises ValueError on y = 0")

    def test_attributes_on_instantiation(self):
        with self.assertRaises(TypeError) as context:
            erroredWidthRect = Rectangle("7", 3, 2, 25)
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(ValueError) as context:
            erroredWidthRect = Rectangle(0, 3, 2, 25)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(TypeError) as context:
            erroredWidthRect = Rectangle(2, "7", 2, 25)
        self.assertEqual(str(context.exception), "height must be an integer")

        with self.assertRaises(ValueError) as context:
            erroredWidthRect = Rectangle(2, -5, 2, 25)
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(ValueError) as context:
            erroredWidthRect = Rectangle(7, 6, -5, 25)
        self.assertEqual(str(context.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as context:
            erroredWidthRect = Rectangle(7, 3, "2", 25)
        self.assertEqual(str(context.exception), "x must be an integer")

        with self.assertRaises(ValueError) as context:
            erroredWidthRect = Rectangle(10, 3, 2, -25)
        self.assertEqual(str(context.exception), "y must be >= 0")

        with self.assertRaises(TypeError) as context:
            erroredWidthRect = Rectangle(2, 7, 2, "25")
        self.assertEqual(str(context.exception), "y must be an integer")

        with self.assertRaises(ValueError) as context:
            erroredWidthRect = Rectangle(7, 6, 2, -25)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_area(self):
        area = TestRectagle.rect.height * TestRectagle.rect.width
        self.assertEqual(TestRectagle.rect.area(), area)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        expected_str = "##\n##\n##"
        TestRectagle.smallRect.display()
        self.assertNotEqual(mock_stdout.getvalue().strip(), expected_str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_imporved_display(self, mock_stdout):
        # smallRect = Rectangle(2, 3, 2, 5)
        expected_str = "\n" * 5 + "  ##\n  ##\n  ##\n"
        TestRectagle.smallRect.display()
        self.assertEqual(mock_stdout.getvalue(), expected_str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_str(self, mock_stdout):
        # rect_with_id = Rectangle(21, 12, 5, 4, 89)
        expected_str = f"[Rectangle] (89) 5/4 - 21/12"
        print(TestRectagle.rect_with_id)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_str)

    def test_update(self):
        TestRectagle.smallRect.update(10, 10, 10, 10, 10)
        self.assertEqual(TestRectagle.smallRect.id, 10)
        self.assertEqual(TestRectagle.smallRect.width(), 10)
        self.assertEqual(TestRectagle.smallRect.height(), 10)
        self.assertEqual(TestRectagle.smallRect.x(), 10)
        self.assertEqual(TestRectagle.smallRect.y(), 10)

    def test_integer_validator(self):
        with self.assertRaises(TypeError) as context:
            TestRectagle.smallRect.integer_validator("num1", "hello")
        self.assertEqual(str(context.exception), "num1 must be an integer")

        with self.assertRaises(ValueError) as context2:
            TestRectagle.smallRect.integer_validator("n", -9)
        self.assertEqual(str(context2.exception), "n must be > 0")

    def test_coordinate_validator(self):
        with self.assertRaises(TypeError) as context:
            TestRectagle.smallRect.coordinate_validator("num1", "hello")
        self.assertEqual(str(context.exception), "num1 must be an integer")

        with self.assertRaises(ValueError) as context2:
            TestRectagle.smallRect.coordinate_validator("n", -9)
        self.assertEqual(str(context2.exception), "n must be >= 0")
