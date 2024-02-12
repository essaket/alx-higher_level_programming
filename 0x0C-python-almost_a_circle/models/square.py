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
