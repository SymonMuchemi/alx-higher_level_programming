#!/usr/bin/python3
"""Child to Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """describes the Rectangle formally and unambiguously

        Returns:
            str: the description
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter method for size attribute"""
        return self.height
    
    @size.setter
    def size(self, value):
        """setter method for the Square instances

        Args:
            value (int): the new value
        """
        self.integer_validator('size', value)
        self.height = value
        self.width = value 
        
    def update(self, *args, **kwargs):
        """update all attributes if using *args or specific 
        attributes if using **kwargs
        """
        if len(args) == 3:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        
        if len(args) == 0:
            for key, val in kwargs.items():
                if key == 'size':
                    self.size = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val
                if key == 'id':
                    self.id = val
