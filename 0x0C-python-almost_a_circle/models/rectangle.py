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
        """checks if the value of an attribute is correct

        Args:
            name (str): the name of the attribute
            value (int): the new attribute value

        Raises:
            TypeError: when the value is not int
            ValueError: when value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def coordinate_validator(self, name, value):
        """checks if the value of an attribute is correct

        Args:
            name (str): name of the attribute
            value (int): new attribute value

        Raises:
            TypeError: when value is not an int
            ValueError: when value is < 0
        """
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

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
            1st argument -> id attribute
            2nd argument -> width attribute
            3rd argument -> height attribute
            4th argument -> x attribute
            5th argument -> y attribute
        """
        if args:
            if len(args) > 0 and args[0] is not None:
                self.id = args[0]
            if len(args) > 1 and args[1] is not None:
                self.integer_validator("width", args[1])
                self.__width = args[1]
            if len(args) > 2 and args[2] is not None:
                self.integer_validator("height", args[2])
                self.__height = args[2]
            if len(args) > 3 and args[3] is not None:
                self.coordinate_validator("x", args[3])
                self.__x = args[3]
            if len(args) > 4 and args[4] is not None:
                self.coordinate_validator("y", args[4])
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.integer_validator("width", value)
                    self.__width = value
                elif key == "height":
                    self.integer_validator("height", value)
                    self.__height = value
                elif key == "x":
                    self.coordinate_validator("x", value)
                    self.__x = value
                elif key == "y":
                    self.coordinate_validator("y", value)
                    self.__y = value
