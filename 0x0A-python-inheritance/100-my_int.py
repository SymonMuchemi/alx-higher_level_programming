#!/usr/bin/python3
"""rebelious class"""


class MyInt(int):
    """simple class that inherits from int"""
    def __new__(cls, value):
        """creates a new instance of MyInt given the integer value

        Args:
            value (int): the integer value

        Returns:
            MyInt: a new instance of MyInt
        """
        return super(MyInt, cls).__new__(cls, value)

    def __eq__(self, other):
        """custom equality comparison of MyInt objects

        Args:
            other (int or MyInt): the object to be compared with

        Returns:
            bool: True if values are not equal, False otherwise
        Raises:
            NotImplemented: if comparison is of non supported objects
        """
        if isinstance(other, int):
            return not super().__eq__(other)
        return NotImplemented

    def __ne__(self, other):
        """custom inequality comparison of MyInt objects

        Args:
            other (MyInt or int): object to be compared with

        Returns:
            bool: True if equal, False otherwise
        """
        if isinstance(other, int):
            return not super().__ne__(other)
        return NotImplemented
