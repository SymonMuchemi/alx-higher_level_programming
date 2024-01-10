#!/usr/bin/python3
"""program to print a ssquare
"""


def print_square(size):
    """prints a square with '#'

    Args:
        size (int): length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return

    square_str = ''
    for i in range(size):
        square_str += "#" * size + "\n"

    print(square_str[:-1])
