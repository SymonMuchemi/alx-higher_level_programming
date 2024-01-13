#!/usr/bin/python3
"""deserializing JSON object programs"""
import json


def from_json_string(my_str):
    """returns a string version of a JSON object

    Args:
        my_str (str): the JSON string

    Returns:
        any: the deserialized JSON object
    """
    return json.loads(my_str)
