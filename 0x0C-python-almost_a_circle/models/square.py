#!/usr/bin/python3
"""Defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Inisialize a new square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns info string of the square"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that assigns attributes"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
