#!/usr/bin/python3
"""Test the base model"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base


class TestBase(unittest.TestCase):
    """test the base model

    Args:
        unittest (TestCase): test cases
    """
    @classmethod
    def setUpClass(cls):
        cls.baseNoId = Base()
        cls.base1 = Base()
        cls.base2 = Base()
        cls.base_with_id = Base(89)

    def test_base_attributes(self):
        self.assertFalse(hasattr(TestBase.base_with_id, '__nb_objects'))
        self.assertTrue(hasattr(TestBase.base_with_id, 'id'))

    def test_id_exists(self):
        self.assertIsNotNone(TestBase.base_with_id.id)
        self.assertIsNotNone(TestBase.baseNoId.id)

    def test_id_as_instantiation(self):
        self.assertEqual(TestBase.base_with_id.id, 89)

    def test_id_increment_by_1(self):
        diff = TestBase.base2.id - TestBase.base1.id
        self.assertEqual(1, diff)

    def test_to_json_string_return_type(self):
        test_dict = {'One': 1, "two": 2}
        test_dict2 = {'One': 1, "two": 2, "Three": 3}

        lst_dict = [test_dict, test_dict2]

        self.assertIsInstance(self.base1.to_json_string(lst_dict), str)

    def test_to_json_string_output(self):
        dict1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        output_str = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(self.base1.to_json_string([dict1]), output_str)

    def test_to_json_string_on_none(self):
        self.assertEqual(self.base1.to_json_string(None), "[]")

    def to_json_string_on_none_dicts(self, list_dictionaries):
        none_dict = "not a dictionary"
        dict1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        mixed_dict = [dict1, none_dict]

        self.assertEqual(self.base1.to_json_string([none_dict]), "[]")
        self.assertEqual(self.base1.to_json_string(mixed_dict), "[]")


if __name__ == "__main__":
    unittest.main()
