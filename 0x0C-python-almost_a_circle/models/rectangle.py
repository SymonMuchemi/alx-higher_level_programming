#!/usr/bin/python3
"""Rectangle class that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle that inherits the Base class

    Args:
        Base (Base): the parent class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the Rectangle class"""
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
        string_output = '\n' * self.y
        for i in range(self.__height):
            string_output += ' ' * self.x
            string_output += '#' * self.__width + '\n'
        print(string_output[:-1])

    def __str__(self):
        """describes the Rectangle formally and unambiguously

        Returns:
            str: the description
        """
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"

    def update(self, *args, **kwargs):
        """update attributes based on arguments or keyworded arguments"""
        if len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]

        if len(args) == 0:
            for key, val in kwargs.items():
                if key == 'width':
                    self.__width = val
                if key == 'height':
                    self.__height = val
                if key == 'x':
                    self.__x = val
                if key == 'y':
                    self.__y = val
                if key == 'id':
                    self.id = val

    def to_dictionary(self):
        """returns the dictionary defination of the class

        Returns:
            dict: dictionary of attributes
        """
        return self.__dict__
