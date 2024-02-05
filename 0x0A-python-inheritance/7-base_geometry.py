#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


class BaseGeometry:
    """A BaseGeometry class"""
    def area(self):
        """raise an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """A method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
