#!/usr/bin/python3
"""Square model"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Child to rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiate the square using the Rectangle
        init method

        Args:
            size (int): the width and height of the square
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (int, optional): identifier number. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of the square instance

        Returns:
            str: representation with attributes
        """
        name = self.__class__.__name__
        id = self.id
        width = self.width
        x = self.x
        y = self.y
        return f"[{name}] ({id}) {x}/{y} - {width}"

    @property
    def size(self):
        """returns the size of the square

        Returns:
            int: the width
        """
        return self.width

    @size.setter
    def size(self, value):
        """setter for the size attribute

        Args:
            value (int): new integer value
        """
        super().integer_validator("width", value=value)
        super().integer_validator("heigh", value=value)

        self.width = value
        self.height = value
