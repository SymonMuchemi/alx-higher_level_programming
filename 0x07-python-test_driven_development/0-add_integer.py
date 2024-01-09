#!/usr/bin/python3
"""simple program to add two integers
"""


def add_integer(a, b=98):
    """sums up two integer

    Args:
        a (int, float): first arg
        b (int, optional): second arg. Defaults to 98.

    Raises:
        TypeError: if a is not an integer or a float
        TypeError: if b is not an integer or a float

    Returns:
        int: the summation result
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
