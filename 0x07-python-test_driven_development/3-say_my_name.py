#!/usr/bin/python3
"""
    Function to print out a name.

"""


def say_my_name(first_name, last_name=""):
    """
    Checks if inputs are actually strings.

    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    """
    Returns a sentence containing both first and last name.

    """
    return ('My name is {} {}'.format(first_name, last_name))
