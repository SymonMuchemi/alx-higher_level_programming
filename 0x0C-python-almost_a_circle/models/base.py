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
        lst_str = []
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        for dictionary in list_dictionaries:
            if not isinstance(dictionary, dict):
                return "[]"
        return json.dumps(list_dictionaries)
