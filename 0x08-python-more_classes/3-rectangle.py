#!/usr/bin/python3
"""module to create a rectangle object
"""


class Rectangle:
    """blueprint for a rectangle object
    """
    def __init__(self, width=0, height=0):
        """constractor for a rectangle object

        Args:
            width (int, optional): the length. Defaults to 0.
            height (int, optional): the height. Defaults to 0.

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter method for retrieving the width

        Returns:
            __width: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle

        Args:
            value (int): the new width

        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter method for retrieving the height

        Returns:
            __height: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the heigth of the rectangle

        Args:
            value (int): the new height

        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """calculates and returns the area of the rectangle

        Returns:
            area: height * width
        """
        return self.__height * self.__width

    def perimeter(self):
        """calculates and returns the perimeter

        Returns:
            perimeter: double the sum of the length and height
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        string_rep = ""
        if (self.__width == 0) or (self.__height == 0):
            return string_rep
        for i in range(self.__height):
            string_rep += "#" * self.__width + "\n"
        return string_rep[:-1]
