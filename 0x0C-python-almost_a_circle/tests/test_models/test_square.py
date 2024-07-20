#!/usr/bin/python3
"""tests for the square model"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square model"""

    def setUp(cls):
        cls.square1 = Square(10, 8, 8)

    def tearDown(self):
        if hasattr(self, 'square1'):
            del self.square1

    def test_square_instantiation_attr(self):
        self.assertIsNotNone(self.square1.id)
        self.assertIsNotNone(self.square1.width)
        self.assertIsNotNone(self.square1.x)
        self.assertIsNotNone(self.square1.y)

        self.assertEqual(self.square1.width, self.square1.height)
        self.assertEqual(self.square1.x, 8)
        self.assertEqual(self.square1.y, 8)

    @patch('sys.stdout', new_callable=StringIO)
    def test_str(self, mock_stdout):
        sq_id = self.square1.id
        expected_str = f"[Square] ({sq_id}) 8/8 - 10"
        print(self.square1)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_str)

    def test_getter(self):
        self.square1.size = 24
        self.assertEqual(self.square1.width, 24)
        self.assertEqual(self.square1.height, 24)

    def test_to_dictionary_return_type(self):
        self.assertIsInstance(self.square1.to_dictionary(), dict)

    def test_to_dictionary_keys(self):
        keys = ['id', 'size', 'x', 'y']
        for key in keys:
            self.assertIn(key, self.square1.to_dictionary().keys())

if __name__ == "__main__":
    unittest.main()
