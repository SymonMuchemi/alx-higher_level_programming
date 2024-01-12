#!/usr/bin/python3
"""functions to add new attributes to objects"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object

    Args:
        obj (any): the object
        name (str): the name of the new attribute
        value (any): the value of the new attribute

    Raises:
        TypeError: if name is not a string or value is None
        TypeError: if unable to add a new attribute
    """
    if not isinstance(name, str):
        raise TypeError("can't add new attribute")
    if value is None:
        raise TypeError("can't add new attribute")
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
