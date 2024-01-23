#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """return the size private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size private attribute value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def __eq__(self, o):
        """Defines the == comparison"""
        return self.__size == o.__size

    def __ne__(self, o):
        """Defines the != comparison"""
        return self.__size != o.__size

    def __gt__(self, o):
        """Defined the > comparison"""
        return self.__size > o.__size

    def __ge__(self, o):
        """Defined the >= comparison"""
        return self.__size >= o.__size

    def __lt__(self, o):
        """Defined the < comparison"""
        return self.__size < o.__size

    def __le__(self, o):
        """Defined the <= comparison"""
        return self.__size <= o.__size
