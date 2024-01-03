#!/usr/bin/python3
"""module to create a square

    This module creates a simple square given a size

    Attributes:
    size: length of each side of the square
"""
error_msg = "position must be a tuple of 2 positive integers"


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

    def __init__(self, size=0, position=(0, 0)):
        """initializes the square with size and position attributes

        Args:
            size (int, optional): the length of the square. Defaults to 0.
            position (tuple, optional): the coordinates. Defaults to (0, 0).

        Raises:
            ValueError: if size is less than or equal to 0
            TypeError: if the size is not an integer
        """
        if not isinstance(size, int):
            raise ValueError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("{}".format(error_msg))

        try:
            x, y = position
        except ValueError:
            raise ValueError(error_msg)

        if not (isinstance(x, int) and isinstance(y, int)) or x < 0 or y < 0:
            raise ValueError("{}".format(error_msg))

        self.__position = position

    @property
    def position(self):
        """getter for the position attribute

        Returns:
            tuple: the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets a new value for the square's position

        Args:
            value (tuple): the new coordinates

        Raises:
            TypeError: if coordinates are not positive
            TypeError: if coordinates are not integers
        """
        if not isinstance(value, tuple):
            raise TypeError("{}".format(error_msg))

        x, y = value

        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("{}".format(error_msg))

        self.__position = value

    def area(self):
        """public instance method that returns square area

        Returns:
            int: the size to the power of 2
        """
        return (pow(self.__size, 2))

    def my_print(self):
        """prints to stdout the square with the character '#'
        """
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
