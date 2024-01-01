#!/usr/bin/python3
"""module to create a square

    This module creates a simple square given a size

    Attributes:
    size: length of each side of the square
"""


class Square:
    """Represents a square shape

    Attributes:
        __size (int): length each side of the square.
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
