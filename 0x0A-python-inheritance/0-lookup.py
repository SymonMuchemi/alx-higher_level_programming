#!/usr/bin/python3
"""Simple function to lookup the names in a scope
"""


def lookup(obj):
    """return a list of available attributes and methods in an
    object

    Args:
        obj (object): the class

    Returns:
        list: methods and attributes
    """
    if obj is not None:
        return (dir(obj))
    return None
