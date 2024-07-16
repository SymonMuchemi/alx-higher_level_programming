#!/usr/bin/python3
"""Rectangle model"""
from models.base import Base


class Rectangle(Base):
    """Child model to Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation"""
        super().__init__(id=id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """retrieve the width property

        Returns:
            int: the private width attribute
        """
        return self.__width

    @property
    def height(self):
        """getter method for height

        Returns:
            int: private height attribute
        """
        return self.__height

    @property
    def x(self):
        """getter for x

        Returns:
            int: private x attribute
        """
        return self.__x

    @property
    def y(self):
        """getter for y

        Returns:
            int: private y attrubute
        """
        return self.__y

    @width.setter
    def width(self, value):
        """changes the values of width

        Args:
            value (int): new value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """changes the values of height

        Args:
            value (int): new value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """changes the values of x

        Args:
            value (int): new value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """changes the values of y

        Args:
            value (int): new value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value
