#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element in a list at index idx
        without modifying the original list

    Args:
        my_list (int): the original list
        idx (int): the index to replace with the new element
        element (any): the new list element

    Returns:
        list: the new list with the replaced element
    """
    if my_list:
        # slicing all the elements in my_list to new_list
        new_list = my_list[:]
        if (idx < len(new_list)) and (idx >= 0):
            new_list[idx] = element
            return new_list
        else:
            return my_list
