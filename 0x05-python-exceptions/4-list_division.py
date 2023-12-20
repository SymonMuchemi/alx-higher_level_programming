#!/usr/bin/python3
def convert_to_integers(lst):
    """converts list elements into integers

    Args:
        lst (any): the array of elements

    Returns:
        list: the final list of integer and or None elements
    """
    final_list = []
    for item in lst:
        try:
            item = int(item)
        except (ValueError, TypeError):
            item = None
        finally:
            final_list.append(item)
    return final_list


def list_division(my_list_1, my_list_2, list_length):
    """divides the elements of two lists

    Args:
        my_list_1 (any): first array
        my_list_2 (any): second array
        list_length (int): the max number of element to be divided

    Returns:
        list: result of element division
    """
    lst1 = convert_to_integers(my_list_1)
    lst2 = convert_to_integers(my_list_2)
    final_list = []
    i = 0
    # max_len = max(len(my_list_1), len(my_list_2))
    for i in range(0, list_length):
        try:
            result = (lst1[i] / lst2[i])
        except (ZeroDivisionError):
            result = 0
            print("division by 0")
        except (TypeError):
            result = 0
            print("wrong type")
        except (IndexError):
            result = 0
            print("out of range")
        finally:
            final_list.append(result)
    return final_list
