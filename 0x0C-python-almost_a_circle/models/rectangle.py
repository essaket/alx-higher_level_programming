#!/usr/bin/python3
"""Defines a rectange class"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """y of ractangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_int("y", value)
        self.__y = value

    def validate_int(self, name, value, eq=True):
        """Method that validat an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))


