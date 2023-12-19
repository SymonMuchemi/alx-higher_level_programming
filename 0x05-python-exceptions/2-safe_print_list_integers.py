#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x integer elements of a list

    Args:
        my_list (list, optional): the collection of elements. Defaults to [].
        x (int, optional): number of elements to be printed. Defaults to 0.

    Returns:
        int: the number of elements printed
    """
    count = 0
    printed = 0
    while printed < x:
        try:
            item = my_list[count]
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                printed += 1
        except (TypeError, IndexError):
            break
        finally:
            count += 1

    print()  # Add a new line after printing the integers
    return printed
