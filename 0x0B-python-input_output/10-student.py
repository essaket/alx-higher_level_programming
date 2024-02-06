#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation
        of a Student instance"""
        try:
            for x in attrs:
                if type(x) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_dict = dict()
        for y, v in self.__dict__.items():
            if y in attrs:
                new_dict[x] = v
        return new_dict
