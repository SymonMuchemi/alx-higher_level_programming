"""tests for the square model"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from models.square import Square


class TestSquare(TestCase):
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
