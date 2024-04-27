#!/usr/bin/python3
# Finds the peak in a list

def find_peak(list_of_integers):
    """ finds a peak in the list and print it out
    
        Finds the largest element in the list
    """
    largest_element = None
    
    if len(list_of_integers) == 0:
        return None
    
    largest_element = list_of_integers[0]
    
    for integer in list_of_integers:
        if integer > largest_element:
            largest_element = integer
    
    return largest_element
