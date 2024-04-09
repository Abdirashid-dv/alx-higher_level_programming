#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """
    Prints the input text with 2 new lines after each of the characters '.', '?', and ':'
    Args:
    :param text: The input text (must be a string)
    :raises TypeError: If the input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text by '.', '?', and ':'
    separators = ['.', '?', ':']
    for sep in separators:
        text = text.replace(sep, sep + '\n\n')

    # Remove any leading/trailing spaces from each line
    lines = text.split('\n')
    formatted_lines = [line.strip() for line in lines]

    # Print the formatted lines
    for line in formatted_lines:
        print(line)
