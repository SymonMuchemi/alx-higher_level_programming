#!/usr/bin/python3
"""simple square base on Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """simple square based on the Rectangle class

    Args:
        Rectangle (BaseGeometry): parent class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """computes square area

        Returns:
            int: size ** 2
        """
        return (pow(self.__size, 2))
