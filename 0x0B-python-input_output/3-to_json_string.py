#!/usr/bin/python3
"""function to serialize a data structure"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of a string object

    Args:
        my_obj (any): the object

    Returns:
        str: the serialize object
    """
    json_rep = json.dumps(my_obj)

    return json_rep
