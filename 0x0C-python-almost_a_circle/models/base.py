#!/usr/bin/python3
"""This is the Base module."""
import json
import os.path


class Base:
    """This is the Base class used to create the almost a circle."""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is the constructor method."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method converts the object list_dictionaries to a json string

        Args:
            list_dictionaries (obj): list of dictionaries.
        Returns:
            Json rep of list_dictionaries or None if list_dictionaried is None
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """This method returns a list of dictionary object representations.

        Args:
            json_string (str): json object representation
        Returns:
            a python data structure
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method saves the json obj rep of list_objs to a file

        Args:
            list_objs (object): list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as jsonfile:
            if list_objs is None:
                dict_list = []
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
            json_string = Base.to_json_string(dict_list)
            jsonfile.write(json_string)

    @classmethod
    def load_from_file(cls):
        """This method loads a python object from a file."""
        filename = cls.__name__ + ".json"
        list_objects = []

        if not os.path.isfile(filename):
            return list_objects

        with open(filename, "r", encoding="utf-8") as jsonfile:
            list_objects = Base.from_json_string(jsonfile.read())

        return [cls.create(**kwargs) for kwargs in list_objects]

    @classmethod
    def create(cls, **dictionary):
        """This method creates an instance of the class with all the attributes
        already set.

        Args:
            dictionary (object): This is a variable number of kw args.
        """
        if cls.__name__ == "Rectangle":
            new_object = cls(1, 1)
        else:
            new_object = cls(1)
        new_object.update(**dictionary)
        return new_object
