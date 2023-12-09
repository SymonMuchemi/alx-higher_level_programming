#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value

    Args:
        a_dictionary (dict): a dictionary

    Returns:
        str: the key
    """
    if a_dictionary is None:
        return None
    best_score_key = None
    max_value = float('-inf')
    for key in a_dictionary:
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
            best_score_key = key
    return best_score_key
