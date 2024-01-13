#!/usr/bin/python3
"""program to write JSON object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes JSON objects to a file

    Args:
        my_obj (any): the object to be serialized
        filename (str): the name of the json file
    """
    with open(filename, 'a', encoding='utf-8') as fp:
        json.dump(my_obj, fp)
