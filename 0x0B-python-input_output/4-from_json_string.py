#!/usr/bin/python3
"""Defines a function returns a JSON"""
import json


def from_json_string(my_str):
    """Method that returns an object represented by a JSON string"""
    return json.loads(my_str)
