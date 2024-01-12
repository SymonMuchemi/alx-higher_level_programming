#!/usr/bin/python3
"""functions to add new attributes to objects"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to the given object.

    Args:
        obj (object): The object to which the attribute will be added.
        name (str): The name of the attribute.
        value (any): The value to set for the attribute.

    Raises:
        TypeError: If the object already has a __doc__ attribute.
    """
    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
