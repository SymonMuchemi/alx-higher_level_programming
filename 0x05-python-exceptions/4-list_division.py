#!/usr/bin/python3 
def verify_list_items(lst):
    """converts list elements into integers

    Args:
        lst (any): the array of elements

    Returns:
        list: the final list of integer and or None elements
    """
    if len(lst) == 0:
        return None
    final_list = []
    for item in lst:
        try:
            item = int(item)
        except(ValueError):
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
    lst1 = verify_list_items(my_list_1)
    lst2 = verify_list_items(my_list_2)
    final_list = []
    count, i = 0, 0
    max_len = max(len(my_list_1), len(my_list_2))
    while (count <= max_len):
        if count == list_length:
            break
        try:
            result = float(lst1[i]) / lst2[i]
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
            count += 1
            i += 1
    return final_list
