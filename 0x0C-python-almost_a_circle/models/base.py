#!/usr/bin/python3
"""Defines a base model class"""
import json
import os
import csv


class Base:
    """class will be the “base” of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file"""
        with open(cls.__name__ + ".json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(cls.to_json_string(list_dicts))

    def from_json_string(json_string):
        """Return the list of json string representation json_string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            new_dict = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_dict = cls(1)
        else:
            new_dict = None
        new_dict.update(**dictionary)
        return new_dict

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        l = []
        list_dicts = [] 
        if os.path.exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", 'r') as file:
                list_dicts = cls.from_json_string(file.read())
                for d in list_dicts:
                    l.append(cls.create(**d))
        return l
