#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new student"""
        self.first_name = first_name
        self.last-name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary representation of a Student instance"""
        return self.__dict__
