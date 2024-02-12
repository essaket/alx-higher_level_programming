#!/usr/bin/python3
"""Defines a base model class"""
import json
import os
import csv


class Base:
    """This class will be the “base” of all other classes in this project"""

    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize a new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
