#!/usr/bin/python3
"""unit test for the Square class"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        """set up stdout to be used in testing
        """
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        """clean up resources or revert any changes made
        during testing
        """
        self.patcher.stop()

    def test_instance_id(self):
        """Test the user ID of the Square instances
        """
        obj1 = Square(21, 6, 1, 4)
        obj2 = Square(25, 10, 20, 256)
        obj3 = Square(45, 99, 78, 2)
        obj4 = Square(24, 6, 9, 3)
        self.assertEqual(obj1.id, 4)
        self.assertEqual(obj2.id, 256)
        self.assertEqual(obj3.id, 2)
        self.assertEqual(obj4.id, 3)

    def test_input(self):
        """test the validator methods"""
        self.assertRaises(ValueError, Square.integer_validator, self, 'test', -10)
        self.assertRaises(ValueError, Square.integer_validator, self, 'test', -20)
        self.assertRaises(ValueError, Square.position_integer_validator, self, 'test', 0)
        self.assertRaises(ValueError, Square.position_integer_validator, self, 'test', -1)

    def test_getters(self):
        """Test the getter methods"""
        obj1 = Square(21, 6, 1, None)
        obj2 = Square(25, 10, 20, 256)
        obj3 = Square(45, 99, 78)
        obj4 = Square(24, 6, 9)
        self.assertEqual(obj1.width, 21)
        self.assertEqual(obj2.width, 25)
        self.assertEqual(obj3.width, 45)
        self.assertEqual(obj4.width, 24)
        
        # test heights
        self.assertEqual(obj1.height, 21)
        self.assertEqual(obj2.height, 25)
        self.assertEqual(obj3.height, 45)
        self.assertEqual(obj4.height, 24)

        #test x
        self.assertEqual(obj1.x, 6)
        self.assertEqual(obj2.x, 10)
        self.assertEqual(obj3.x, 99)
        self.assertEqual(obj4.x, 6)
        
        # test y
        self.assertEqual(obj1.y, 1)
        self.assertEqual(obj2.y, 20)
        self.assertEqual(obj3.y, 78)
        self.assertEqual(obj4.y, 9)

    def test_setters(self):
        """test the setter method of the class"""
        mySquare = Square(25, 10, 20, 256)
        
        self.assertEqual(mySquare.size, 25)
        self.assertEqual(mySquare.x, 10)
        self.assertEqual(mySquare.y, 20)
        self.assertEqual(mySquare.id, 256)
        
        # changing size
        
        mySquare.size = 10
        
        self.assertEqual(mySquare.size, 10)
        
    def test_update(self):
        """tests the update method
        """
        obj = Square(10, 1, 1, 1)
        
        # Before change
        self.assertEqual(obj.size, 10)
        self.assertEqual(obj.x, 1)
        self.assertEqual(obj.y, 1)
        self.assertEqual(obj.id, 1)
        
        # changing attributes
        obj.update(y=1, size=2, x=3, id=89)        
        
        # after
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 1)
        self.assertEqual(obj.id, 89)

    def test_description(self):
        """tests the __str__ method"""
        myRect = Square(4, 4, 1, 254)
        
        with patch('sys.stdout', new_callable=StringIO) as mock_std:
            print(myRect)
        
        expected_desc = '[Square] (254) 4/1 - 4'
        self.assertEqual(mock_std.getvalue().strip(), expected_desc)
