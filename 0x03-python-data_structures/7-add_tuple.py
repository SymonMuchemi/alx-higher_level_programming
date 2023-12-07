#!/usr/bin/python3

def check_tuple_size(my_tuple):
    if (len(my_tuple) == 0):
        new_tuple = tuple((0, 0))
        return new_tuple
    elif (len(my_tuple) == 1):
        new_tuple == tuple((my_tuple[0], 0))
        return new_tuple
    else:
        return my_tuple


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check_tuple_size(tuple_a)
    tuple_b = check_tuple_size(tuple_b)
    
    x = tuple_a[0] + tuple_b[0]
    y = tuple_a[1] + tuple_b[1]
    
    return tuple((x, y))
