#!/usr/bin/python3
"""basic geometry class parents Rectangle"""


class BaseGeometry:
    """simple class"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (str): an identifier
            value (int): a integer number

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value


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

