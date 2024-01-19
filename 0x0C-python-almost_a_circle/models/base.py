#!/usr/bin/python3
"""a base class"""


class Base:
    """base class that manages the number of instances
    and avoid duplication
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
