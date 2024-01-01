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

    Raises:
        ValueError: if the size is initialized to 0 or less than 0
        TypeError: if the size is not an integer
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """getter method

        Returns:
            int: the length of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of square length

        Args:
            value (int): the new length to be set

        Raises:
            ValueError: if the value is less than or equal to 0
            TypeError: if the value is not an integer
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """public instance method that returns square area

        Returns:
            int: the size to the power of 2
        """
        return (pow(self.__size, 2))

    def my_print(self):
        """prints to stdout the square with the character '#'
        """
        length = self.__size
        if length > 0:
            for i in range(length):
                print("{}".format("#" * self.__size))
        else:
            print()
