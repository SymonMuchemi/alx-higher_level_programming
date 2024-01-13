#!/usr/bin/python3
"""function to create objects from json files"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file

    Args:
        filename (str): the name of the file

    Returns:
        any: the created object
    """
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)
