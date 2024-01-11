#!/usr/bin/python3
"""basic geometry class parents Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initializes the rectangle using integer_validate()

        Args:
            width (int): the length
            height (int): the height
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
        super().__init__()
