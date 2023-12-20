#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides the elements of two lists

    Args:
        my_list_1 (any): first array
        my_list_2 (any): second array
        list_length (int): the max number of element to be divided

    Returns:
        list: result of element division
    """
    final_list = []
    i = 0
    # max_len = max(len(my_list_1), len(my_list_2))
    for i in range(0, list_length):
        try:
            result = (my_list_1[i] / my_list_2[i])
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
