#!/usr/bin/python3
"""Difines an object attribute lookup function"""


def lookup(obj):
    """returns the list of available attributes and methods"""
    return dir(obj)
