#!/usr/bin/python3
"""
This is module "3-say_my-name"
Defines a function say_my_name
"""

def say_my_name(first_name, last_name=""):
    """
     Prints the full name in the format "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    full_name = f"My name is {first_name} {last_name}"
    print(full_name)

