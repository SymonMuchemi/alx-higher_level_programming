#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurences of an element in a list

    Args:
        my_list (int): the array of integers
        search (int): the item to be replaced
        replace (int): the item to replace search with
    """
    if len(my_list) == 0:
        return my_list
    else:
        new_list = []
        for i in my_list:
            if i == search:
                new_list.append(replace)
            else:
                new_list.append(i)
        return new_list
