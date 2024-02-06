#!/usr/bin/python3
"""Defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Method that inserts a line of text to a file,
    after each line containing a specific string"""
    new_text = ""
    with open(filename, 'r') as file:
        for line in file:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, 'w') as file:
        file.write(new_text)
