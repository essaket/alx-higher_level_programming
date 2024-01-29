#!/usr/bin/python3
"""
Write an empty class Rectangle that defines a rectangle
"""



class Rectangle:
    """Defines an empty Rectangle"""
     def __init__(self, width=0, height=0):
        """Initialize the Rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the width private attribute value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width private attribute value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height private attribute value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height private attribute value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
