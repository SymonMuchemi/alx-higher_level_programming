#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """print a given list in reverse order

    Args:
        my_list (list, optional): the list. Defaults to [].
    """
    if my_list:
        my_list = my_list[::-1]
        for item in my_list:
            print("{:d}".format(item))
