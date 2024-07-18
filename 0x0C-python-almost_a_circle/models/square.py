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

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        if args:
            if len(args) > 0 and args[0] is not None:
                self.id = args[0]
            if len(args) > 1 and args[1] is not None:
                super().integer_validator("size", args[1])
                self.size = args[1]
            if len(args) > 2 and args[2] is not None:
                super().coordinate_validator("x", args[2])
                self.x = args[2]
            if len(args) > 3 and args[3] is not None:
                super().coordinate_validator("y", args[3])
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    super().integer_validator("height", value)
                    self.size = value
                elif key == "x":
                    super().coordinate_validator("x", value)
                    self.x = value
                elif key == "y":
                    super().coordinate_validator("y", value)
                    self.y = value
