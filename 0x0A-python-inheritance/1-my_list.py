#!/usr/bin/python3
"""Defines an inherited list class MyList"""


class MyList(list):
    """class MyList inherits from list"""
    def print_sorted(self):
        """prints the list in sorted ascending order"""
        print(sorted(self))
