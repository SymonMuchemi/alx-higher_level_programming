#!/usr/bin/python3
"""Student with a to_json method"""


class Student:
    """Student blueprint
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a list of specific attributes

        Args:
            attrs (list, optional): list of strings. Defaults to None.

        Returns:
            dict: dictionary description with specified attributes
        """
        if attrs is None:
            return self.__dict__
        else:
            specific_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    specific_dict[attr] = self.__dict__[attr]
            return specific_dict
