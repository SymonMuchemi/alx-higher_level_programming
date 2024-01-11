#!/usr/bin/python3

def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of the specified class

    Args:
        obj (any): suspected child
        a_class (class): a class

    Returns:
        True or False: if the object is an instance of the class
    """
    return (type(obj) == a_class)
