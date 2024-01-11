#!/usr/bin/python3
"""program to check parent instance relationship
"""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of the specified class

    Args:
        obj (any): suspected child
        a_class (class): a class

    Returns:
        True or False: if the object is an instance of the class
    """
    return (type(obj) is a_class)
