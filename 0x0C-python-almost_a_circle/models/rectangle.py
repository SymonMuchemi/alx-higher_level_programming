#!/usr/bin/python3
"""Rectangle class that inherits from base"""
from models.base import Base

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
        
        
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            raise ValueError("height must be > 0")
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if value > 0:
            self.__x = value
        else:
            raise ValueError("x must be > 0")
        
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if value > 0:
            self.__y = value
        else:
            raise ValueError("y must be > 0")
