#!/usr/bin/python3
"""
This module contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public attr area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
