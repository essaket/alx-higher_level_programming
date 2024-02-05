#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass representing a rectangle"""
    def __init__(self, size):
        """Initialize"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return the area of square"""
        return self.__size ** 2
