#!/usr/bin/python3
"""Defines a file-writing function"""


def write_file(filename="", text=""):
    """Method that writes a string to a text file
    and returns the number of characters written"""
    with open(filename, 'w') as file:
        return file.write(text)
