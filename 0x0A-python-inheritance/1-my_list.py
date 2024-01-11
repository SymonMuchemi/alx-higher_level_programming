#!/usr/bin/python3
"""class that inherits from the list class """


class MyList(list):
    """simple list

    Args:
        list (list): list
    """
    def print_sorted(self):
        """print the sorted version of the list
        """
        sorted_list = sorted(self)
        print(sorted_list)
