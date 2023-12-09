#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """returns all elements present in only one set

    Args:
        set_1 (set): first set
        set_2 (set): second set

    Returns:
        set: all elements in one set
    """
    difference_set = (set_1 | set_2) - (set_1 & set_2)
    return difference_set
