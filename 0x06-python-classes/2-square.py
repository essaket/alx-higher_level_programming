#!/usr/bin/python3
"""Square Class"""


class Square:
    """Initialize a new Square"""
    def __init__(self, size):
        """
        Arg:
            size: a integer representing object size.
                  has a default value of 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
