#!/usr/bin/python3
"""Defines a python class to JSON fuction"""


def class_to_json(obj):
    """Returns the dictionary represntation of a simple data structure"""
    return obj.__dict__
