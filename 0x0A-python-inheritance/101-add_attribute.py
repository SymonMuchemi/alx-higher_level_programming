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
    if isinstance(name, str) and value != None:
        try:
            setattr(obj, name, value)
        except AttributeError as e:
            raise TypeError("can't add new attribute")
    else:
        raise TypeError("can't add new attribute")
