#!/usr/bin/python3
"""The parent model"""
import json


class Base():
    """parent model"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        lst_str = []
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        for dictionary in list_dictionaries:
            if not isinstance(dictionary, dict):
                return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of child object instances
        """
        filename = cls.__name__ + '.json'

        if list_objs is None:
            list_objs = []

        list_of_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_of_dicts)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a JSON string representation into a Python object.

        Args:
            json_string (str): The JSON string to be deserialized.

        Returns:
            list: The deserialized Python object.

        """
        if json_string is None:
            return []

        return json.loads(json_string)
