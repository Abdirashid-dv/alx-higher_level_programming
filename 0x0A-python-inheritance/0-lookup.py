#!/usr/bin/python3
"""
this module contains the lookup function
"""


def lookup(obj):
    """returns a list of available attr and methods of an object"""
    return dir(obj)
