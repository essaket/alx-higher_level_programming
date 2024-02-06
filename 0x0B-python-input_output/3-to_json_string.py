#!/usr/bin/python3
"""definds a file creates JSON"""
import json


def to_json_string(my_obj):
    """Method that return the JSON representation of an object"""
    return json.dumps(my_obj)
