#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary

    Args:
        a_dictionary (dict): the dictionary
        key (str, optional): the key to delete. Defaults to "".

    Returns:
        dict: the new dictionary
    """
    if key in a_dictionary:
        a_dictionary.pop(key)
        return a_dictionary
    return a_dictionary
