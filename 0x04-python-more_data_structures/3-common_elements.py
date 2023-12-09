#!/usr/bin/python3
def common_elements(set_1, set_2):
    """returns a set of all common elements in two sets

    Args:
        set_1 (set): first set
        set_2 (set): second set

    Returns:
        set: common elements
    """
    intersection = set(set_1 & set_2)
    return intersection
