#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replaces a list item at a given index

    Args:
        my_list (int): the list to change
        idx (int): the index
        element (int): the new element

    Returns:
        int: the new or original list
    """
    if (idx < 0) or (idx >= len(my_list)):
        return my_list
    my_list[idx] = element
    return my_list
