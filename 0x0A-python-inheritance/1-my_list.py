#!/usr/bin/python3
"""
This module contains MyList class
"""


class MyList(list):
    """this a subclass of list"""

    def __init__(self):
        """initialize the obj"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
