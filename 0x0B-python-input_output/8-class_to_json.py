#!/usr/bin/python3
"""program to return dictionary description  of data structures"""


def class_to_json(obj):
    """function that return the dictionary description for JSON serialization
    object

    Args:
        obj (any): the object

    Returns:
        dict: a dictionary representation
    """
    if obj is not None:
        return obj.__dict__
    else:
        return {}
