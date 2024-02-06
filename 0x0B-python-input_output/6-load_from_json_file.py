#!/usr/bin/python3
"""Defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Method that creates an Object from a “JSON file”."""
    with open(filename, 'r') as file:
        return json.load(file)
