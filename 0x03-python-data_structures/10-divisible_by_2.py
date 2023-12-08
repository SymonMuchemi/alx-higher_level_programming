#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list

    Args:
        my_list (list, optional): the list of numbers. Defaults to [].

    Returns:
        list: a list of boolean value pointing to list item positions
    """
    bool_list = []
    for num in my_list:
        if num % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return list(bool_list)
