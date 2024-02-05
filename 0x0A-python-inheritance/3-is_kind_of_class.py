#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    '''Determines if an object is a subclass of a class.'''
    return True if isinstance(obj, a_class) else False
