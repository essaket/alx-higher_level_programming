#!/usr/bin/python3
"""Defines a file-append function"""


def append_write(filename="", text=""):
    """Method that appends a string at the end of a
    text file and returns the number of characters added"""
    with open(filename, 'a') as file:
        return file.write(text)
