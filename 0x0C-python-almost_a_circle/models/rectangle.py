#!/usr/bin/python3
"""Rectangle class that inherits from base"""
from models.base import Base
        
        
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.position_integer_validator('x', x)
        self.position_integer_validator(y, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    
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
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
        
    def position_integer_validator(self, name, value):
        """validates the value of a position variable

        Args:
            name (str): name of the position attribute/variable
            value (int): a integer number

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be >= 0".format(name))
        
    @property
    def width(self):
        """width's getter method"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """sets a new value of width

        Args:
            value (int): the new value
        """
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets a new value for the height attribute

        Args:
            value (int): the new value
        """
        self.integer_validator("height", value)
        self.__height = value
    
    @property
    def x(self):
        """x's getter method"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """sets a new value for the attribute x

        Args:
            value (int): the new value
        """
        self.position_integer_validator('x', value)
        self.__x = value
        
    @property
    def y(self):
        """y's getter method"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """sets a new value for the attribute y

        Args:
            value (int): the new value
        """
        self.position_integer_validator("y", value)
        self.__y = value

    def area(self):
        """computes the area of the rectangle

        Returns:
            int: height * width
        """
        return (self.__height * self.__width)
    
    def display(self):
        """prints in the stdout the Rectangle instance with the
        character '#'
        """
        string_output = ''
        for i in range(self.__height):
            string_output += '#' * self.__width + '\n'
        print(string_output[:-1])

    def __str__(self):
        """describes the Rectangle formally and unambiguously

        Returns:
            str: the description
        """
        return f"[Rectangle] ({self.id}) <{self.x}>/<{self.y}> - <{self.width}>/<{self.height}>"
