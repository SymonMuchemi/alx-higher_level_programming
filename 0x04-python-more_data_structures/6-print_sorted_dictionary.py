#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """sorts a dictionary and prints it

    Args:
        a_dictionary (dict): the dictionary
    """
    sorted_dict = sorted(a_dictionary.keys())
    for key in sorted_dict:
        val = a_dictionary[key]
        print(f"{key}: {val}")
