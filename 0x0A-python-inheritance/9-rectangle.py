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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area"""
        return (self.__height * self.__width)

    def __repr__(self):
        """returns a string representation

        Returns:
            str: representation
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
