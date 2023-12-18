#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x number of elements in a list

    Args:
        my_list (list, optional): the list of elements. Defaults to [].
        x (int, optional): the number of elements. Defaults to 0.
    Return:
        the real number of elements printed
    """
    i = 0
    num_str = ""
    while ((i < x) and (x > 0)):
        try:
            num_str += str(my_list[i])
            i += 1
        except IndexError:
            break
    print("{}".format(num_str))
    return (i)
