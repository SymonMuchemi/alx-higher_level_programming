#!/usr/bin/python3
"""program to check parent instance relationship
"""


def inherits_from(obj, a_class):
    """checks if an object is a inherits from a specified class

    Args:
        obj (any): suspected child
        a_class (class): a class

    Returns:
        True or False: if the object is an instance of the class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
