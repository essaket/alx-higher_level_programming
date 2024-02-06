#!/usr/bin/python3
"""Defines a text file-reading function"""


def read_file(filename=""):
    """Methods that reads a text file and prints it"""
    with open(filename, 'r') as file:
        print(file.read(), end="")
