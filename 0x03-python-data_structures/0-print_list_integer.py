#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """print a list of integers

    Args:
        my_list (list, optional): the list of integers to be printed. Defaults to [].
    """
    for item in my_list:
        print("{}".format(item))
