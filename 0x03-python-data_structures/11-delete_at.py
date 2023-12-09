#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """deletes an element from a list

    Args:
        my_list (list, optional): the list of elements. Defaults to [].
        idx (int, optional): the index of deletion. Defaults to 0.
    Return:
        list: the list without an element or the original
    """
    if idx >= len(my_list) or (idx < 0):
        return my_list
    my_list[:] = my_list[:idx] + my_list[idx+1:]
    return my_list
