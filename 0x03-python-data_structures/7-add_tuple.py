#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds the elements of two tuples together

    Args:
        tuple_a (tuple, optional): the first tuple. Defaults to ().
        tuple_b (tuple, optional): the second tuple. Defaults to ().

    Returns:
        tuple: the sum of the elements of the two tuples
    """
    a = (0, 0)
    b = (0, 0)

    if len(tuple_a) == 0:
        a = (0, 0)
    elif len(tuple_a) == 1:
        a = (tuple_a[0], 0)
    elif len(tuple_a) >= 2:
        a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 0:
        b = (0, 0)
    elif len(tuple_b) == 1:
        b = (tuple_b[0], 0)
    elif len(tuple_b) >= 2:
        b = (tuple_b[0], tuple_b[1])

    return (a[0] + b[0], a[1] + b[1])
