#!/usr/bin/python3

def element_at(my_list, idx):
    """retrieves an element from a list

    Args:
        my_list (int): the list of elements
        idx (int): the index

    Returns:
        int: the element at index idx
    """
    length = len(my_list)
    if (idx >= length) or (idx < 0):
        return None
    else:
        return my_list[idx]
