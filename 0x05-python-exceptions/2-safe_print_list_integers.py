#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list

    Args:
        my_list (list, optional): the collection of elements. Defaults to [].
        x (int, optional): number of elements to be printed. Defaults to 0.

    Returns:
        int: the number of elements printed
    """
    num_str = ""
    i = 0
    while ((i < x) and (x > 0)):
        try:
            item = int(my_list[i])
            num_str += str(item)
            i += 1
        except (ValueError, TypeError, IndexError):
            break
    print("{:d}".format(int(num_str)))
    return (i)
