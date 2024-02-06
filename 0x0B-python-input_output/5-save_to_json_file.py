#!/usr/bin/python3
"""Defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Method that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, 'w') as file:
        return json.dump(my_obj, file)
