#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle as Rect


class TestRect(unittest.TestCase):
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
        """Test the user ID of the Rect instances
        """
        obj1 = Rect(21, 2, 6, 1, 4)
        obj2 = Rect(25, 9, 10, 20, 256)
        obj3 = Rect(45, 78, 99, 78, 2)
        obj4 = Rect(24, 87, 6, 9, 3)
        self.assertEqual(obj1.id, 4)
        self.assertEqual(obj2.id, 256)
        self.assertEqual(obj3.id, 2)
        self.assertEqual(obj4.id, 3)

    def test_input(self):
        """test the validator methods"""
        self.assertRaises(ValueError, Rect.integer_validator, self, 'test', -10)
        self.assertRaises(ValueError, Rect.integer_validator, self, 'test', -20)
        self.assertRaises(ValueError, Rect.position_integer_validator, self, 'test', 0)
        self.assertRaises(ValueError, Rect.position_integer_validator, self, 'test', -1)

    def test_getters(self):
        """Test the getter methods"""
        obj1 = Rect(21, 2, 6, 1, None)
        obj2 = Rect(25, 9, 10, 20, 256)
        obj3 = Rect(45, 78, 99, 78)
        obj4 = Rect(24, 87, 6, 9)
        self.assertEqual(obj1.width, 21)
        self.assertEqual(obj2.width, 25)
        self.assertEqual(obj3.width, 45)
        self.assertEqual(obj4.width, 24)
        
        # test heights
        self.assertEqual(obj1.height, 2)
        self.assertEqual(obj2.height, 9)
        self.assertEqual(obj3.height, 78)
        self.assertEqual(obj4.height, 87)

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
        myRect = Rect(25, 9, 10, 20, 256)
        myRect.width = 1
        myRect.height = 1
        myRect.x = 1
        myRect.y = 1
        
        self.assertEqual(myRect.width, 1)
        self.assertEqual(myRect.height, 1)
        self.assertEqual(myRect.x, 1)
        self.assertEqual(myRect.y, 1)

    def test_area(self):
        """test the value of area"""
        myRect = Rect(1, 2, 99, 78)
        myRect1 = Rect(5, 7, 99, 78)
        myRect2 = Rect(4, 8, 99, 78)
        
        self.assertAlmostEqual(myRect.area(), 2)
        self.assertAlmostEqual(myRect1.area(), 35)
        self.assertAlmostEqual(myRect2.area(), 32)

    def test_display(self):
        """test the display method"""
        myRect = Rect(5, 2, 99, 78)
        
        # redirect stdout to capture print output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            myRect.display()
        
        # verify printed output matches expected pattern
        expected_output = '#####\n#####'
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_square_rectangle(self):
        """test when width == height"""
        myRect = Rect(4, 4, 1, 1, 21)
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            myRect.display()
        
        expected_output = '####\n####\n####\n####'
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_description(self):
        """tests the __str__ method"""
        myRect = Rect(4, 4, 1, 1, 254)
        
        with patch('sys.stdout', new_callable=StringIO) as mock_std:
            print(myRect)
        
        expected_desc = '[Rectangle] (254) 1/1 - 4/4'
        self.assertEqual(mock_std.getvalue().strip(), expected_desc)
