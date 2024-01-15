#!/usr/bin/python3
"""Student with a to_json method"""


class Student:
    """Student blueprint
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets the dictionary of class attributes

        Returns:
            dict: dictionary description of the class
        """
        return self.__dict__
