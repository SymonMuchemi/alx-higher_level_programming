#!/usr/bin/python3
"""module to create a rectangle object
"""


class Rectangle:
    """blueprint for a rectangle object
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """constractor for a rectangle object
        and keeps count of number of instances created

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
        Rectangle.number_of_instances += 1

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
        """define a string representation of the rectangle

        Returns:
            string_rep (str): string representation using '#'
        """
        s = ''
        if self.__width > 0 and self.__height > 0:
            for _ in range(self.__height):
                for _ in range(self.__width):
                    s += str(self.print_symbol)
                s += '\n'
        return s[: -1]

    def __repr__(self):
        """provides a formal and unambiguous representaion

        Returns:
            statement: formal rep of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """detects deletion an prints a message
            and decrements the instance count
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
