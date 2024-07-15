#!/usr/bin/python3
"""The parent model"""


class Base():
    """parent model"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id == None:
            self.id = Base.__nb_objects + 1
        else:
            self.id = id
