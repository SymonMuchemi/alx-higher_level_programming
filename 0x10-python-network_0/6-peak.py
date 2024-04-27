#!/usr/bin/python3
""" function finds the peak value in a list on integers

    The list is iterated from first element to the last and the 
    largest value is found and returned
    """

def find_peak(list_of_integers):
    """finds the peak in a list

    Args:
        list_of_integers (int): the array of integers

    Returns:
        int: the largest integer in the list
    """
    largest_element = None

    if len(list_of_integers) == 0:
        return None

    largest_element = list_of_integers[0]

    for integer in list_of_integers:
        if integer > largest_element:
            largest_element = integer

    return largest_element
