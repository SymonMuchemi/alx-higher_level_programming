#!/usr/bin/python3
"""Rectangle model"""
from models.base import Base


class Rectangle(Base):
    """Child model to Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation"""
        super().__init__(id=id)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.coordinate_validator("x", x)
        self.coordinate_validator("y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def coordinate_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
    
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
        self.integer_validator("width", value=value)
        self.__width = value

    @height.setter
    def height(self, value):
        """changes the values of height

        Args:
            value (int): new value
        """
        self.integer_validator("height", value=value)
        self.__height = value

    @x.setter
    def x(self, value):
        """changes the values of x

        Args:
            value (int): new value
        """
        self.coordinate_validator("x", value=value)
        self.__x = value

    @y.setter
    def y(self, value):
        """changes the values of y

        Args:
            value (int): new value
        """
        self.coordinate_validator("y", value=value)
        self.__y = value

    def area(self):
        """calculates the area of the rectangle instance

        Returns:
            int: width multiplied by height
        """
        return self.__width * self.__height

    def display(self):
        """prints a rectangle of #'s
        """
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """string representation of the Rectangle instance

        Returns:
            str: representation with attributes
        """
        name = self.__class__.__name__
        id = self.id
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        return f"[{name}] ({id}) {x}/{y} - {width}/{height}"

    def update(*args):
        if args[0] and isinstance(args[0], int):
            self.id = args[0]
            
