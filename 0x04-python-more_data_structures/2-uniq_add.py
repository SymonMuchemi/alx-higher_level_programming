#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all uniq integers in a list

    Args:
        my_list (list, optional): array of integers. Defaults to [].

    Returns:
        int: the summation of all unique numbers
    """
    if len(my_list) == 0:
        return 0
    else:
        uniq_nums = set({})
        for i in my_list:
            uniq_nums.add(i)    
        # adding the unique numbers
        sum = 0
        for n in uniq_nums:
            sum += n
        return sum
