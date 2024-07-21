#!/usr/bin/python3
"""tests for the Rectangle"""
import unittest
import os
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class"""

    @classmethod
    def setUpClass(cls):
        cls.rect = Rectangle(21, 12, 5, 4)
        cls.rect_with_id = Rectangle(21, 12, 5, 4, 89)
        cls.smallRect = Rectangle(2, 3, 2, 5)
        cls.newRect = Rectangle(9, 9, 9, 9, 8)
        cls.noXRect = Rectangle(10, 10)
        cls.noYRect = Rectangle(10, 10, 9)
        cls.xyRect = Rectangle(1, 2)

    @classmethod
    def tearDown(cls):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_rectangle_parent_class(self):
        self.assertIsInstance(self.rect, Base)

    def test_rectangle_instantiation(self):
        self.assertEqual(self.xyRect.width, 1)
        self.assertEqual(self.xyRect.height, 2)
        self.assertEqual(self.xyRect.x, 0)
        self.assertEqual(self.xyRect.y, 0)
        self.assertIsNotNone(self.xyRect.id)

    def test_rectangle_height_zero(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_rectangle_width_zero(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_rectangle_attributes(self):
        self.assertFalse(hasattr(self.rect, '__width'))
        self.assertFalse(hasattr(self.rect, '__height'))
        self.assertFalse(hasattr(self.rect, '__x'))
        self.assertFalse(hasattr(self.rect, '__y'))

    def test_width_getter(self):
        self.assertEqual(self.rect.width, 21)

    def test_height_getter(self):
        self.assertEqual(self.rect.height, 12)

    def test_x_getter(self):
        self.assertEqual(self.rect.x, 5)

    def test_y_getter(self):
        self.assertEqual(self.rect.y, 4)

    def test_height_setter(self):
        self.rect.height = 32
        self.assertEqual(self.rect.height, 32)

    def test_width_setter(self):
        self.rect.width = 32
        self.assertEqual(self.rect.width, 32)

    def test_x_setter(self):
        self.rect.x = 10
        self.assertEqual(self.rect.x, 10)

    def test_y_setter(self):
        self.rect.y = 10
        self.assertEqual(self.rect.y, 10)

    def test_width_setter_raises_TypeError(self):
        with self.assertRaises(TypeError) as context:
            self.rect.width = "Mellon"
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_setter_raises_ValueError(self):
        with self.assertRaises(ValueError) as context:
            self.rect.width = -90
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_height_setter_raises_TypeError(self):
        with self.assertRaises(TypeError) as context:
            self.rect.height = "Mellon"
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_setter_raises_ValueError(self):
        with self.assertRaises(ValueError) as context:
            self.rect.height = -90
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_x_setter_raises_TypeError(self):
        with self.assertRaises(TypeError) as context:
            self.rect.x = "Mellon"
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_y_setter_raises_TypeError(self):
        with self.assertRaises(TypeError) as context:
            self.rect.y = "Mellon"
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_x_raises_ValueError(self):
        with self.assertRaises(ValueError) as context:
            self.rect.x = -6
        self.assertEqual(str(context.exception), "x must be >= 0")

        try:
            self.rect.x = 0
        except ValueError:
            self.fail("x.setter raises ValueError on x = 0")

    def test_y_raises_ValueError(self):
        with self.assertRaises(ValueError) as context:
            self.rect.y = -6
        self.assertEqual(str(context.exception), "y must be >= 0")

        try:
            self.rect.y = 0
        except ValueError:
            self.fail("y.setter raises ValueError on y = 0")

    def test_attributes_on_instantiation(self):
        with self.assertRaises(TypeError) as context:
            Rectangle("7", 3, 2, 25)
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(ValueError) as context:
            Rectangle(0, 3, 2, 25)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(TypeError) as context:
            Rectangle(2, "7", 2, 25)
        self.assertEqual(str(context.exception), "height must be an integer")

        with self.assertRaises(ValueError) as context:
            Rectangle(2, -5, 2, 25)
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(ValueError) as context:
            Rectangle(7, 6, -5, 25)
        self.assertEqual(str(context.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as context:
            Rectangle(7, 3, "2", 25)
        self.assertEqual(str(context.exception), "x must be an integer")

        with self.assertRaises(ValueError) as context:
            Rectangle(10, 3, 2, -25)
        self.assertEqual(str(context.exception), "y must be >= 0")

        with self.assertRaises(TypeError) as context:
            Rectangle(2, 7, 2, "25")
        self.assertEqual(str(context.exception), "y must be an integer")

        with self.assertRaises(ValueError) as context:
            Rectangle(7, 6, 2, -25)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_area(self):
        area = self.rect.height * self.rect.width
        self.assertEqual(self.rect.area(), area)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        expected_str = "\n" * 5 + "  ##\n  ##\n  ##\n"
        self.smallRect.display()
        self.assertEqual(mock_stdout.getvalue(), expected_str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_without_x_y(self, mock_stdout):
        r = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"

        r.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_without_y(self, mock_stdout):
        r = Rectangle(4, 3, 0)
        expected_output = "####\n####\n####\n"

        r.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_str(self, mock_stdout):
        expected_str = "[Rectangle] (89) 5/4 - 21/12"
        print(self.rect_with_id)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_str_rect_with_no_x_y(self, mock_stdout):
        xyRect_id = self.xyRect.id
        xyRect_str = f"[Rectangle] ({xyRect_id}) 0/0 - 1/2"
        print(self.xyRect)
        self.assertEqual(mock_stdout.getvalue().strip(), xyRect_str)

    def test_integer_validator(self):
        with self.assertRaises(TypeError) as context:
            self.smallRect.integer_validator("num1", "hello")
        self.assertEqual(str(context.exception), "num1 must be an integer")

        with self.assertRaises(ValueError) as context:
            self.smallRect.integer_validator("n", -9)
        self.assertEqual(str(context.exception), "n must be > 0")

    def test_coordinate_validator(self):
        with self.assertRaises(TypeError) as context:
            self.smallRect.coordinate_validator("num1", "hello")
        self.assertEqual(str(context.exception), "num1 must be an integer")

        with self.assertRaises(ValueError) as context:
            self.smallRect.coordinate_validator("n", -9)
        self.assertEqual(str(context.exception), "n must be >= 0")

    def test_id_update(self):
        self.rect.update(89)
        self.assertEqual(self.rect.id, 89)

    def test_id_width_update(self):
        self.rect.update(8, 21)
        self.assertEqual(self.rect.id, 8)
        self.assertEqual(self.rect.width, 21)

    def test_id_width_height_update(self):
        self.rect.update(8, 21, 25)
        self.assertEqual(self.rect.id, 8)
        self.assertEqual(self.rect.width, 21)
        self.assertEqual(self.rect.height, 25)

    def test_x_update(self):
        self.assertNotEqual(self.rect.x, 3)
        self.rect.update(8, 21, 25, 3)
        self.assertEqual(self.rect.x, 3)
        self.rect.update(8, 21, 25, 5)

    def test_update_with_kwargs(self):
        self.assertNotEqual(self.newRect.id, 32)
        self.assertNotEqual(self.newRect.width, 32)
        self.assertNotEqual(self.newRect.height, 32)
        self.assertNotEqual(self.newRect.x, 32)
        self.assertNotEqual(self.newRect.y, 32)

        self.newRect.update(id=32, width=32, x=32, y=32, height=32)
        self.assertEqual(self.newRect.id, 32)
        self.assertEqual(self.newRect.height, 32)
        self.assertEqual(self.newRect.width, 32)
        self.assertEqual(self.newRect.x, 32)
        self.assertEqual(self.newRect.y, 32)

    def test_to_dictionary_return_type(self):
        self.assertIsInstance(self.rect.to_dictionary(), dict)

    def test_to_dictionary_keys(self):
        keys = ['x', 'y', 'width', 'height', 'id']

        for key in keys:
            self.assertIn(key, self.rect.to_dictionary().keys())
        self.assertIsInstance(self.rect.to_dictionary(), dict)

    def test_save_to_file(self):
        Rectangle.save_to_file([self.rect, self.rect_with_id, self.newRect])

        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json") as file:
            content = file.read()

        self.assertNotEqual(content, "[]")

    def test_create(self):
        new_dict = {'id': 404, 'size': 3, 'x': 4, 'y': 5}
        new = Rectangle.create(**new_dict)

        self.assertIsInstance(new, Rectangle)
        self.assertTrue(hasattr(new, 'id'))

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        output = Rectangle.load_from_file()

        self.assertIsInstance(output, list)
        self.assertIsInstance(output[0], Rectangle)
        self.assertIsInstance(output[1], Rectangle)

    def test_load_from_file_returns_empty_list(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        self.assertEqual(Rectangle.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
