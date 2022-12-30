#!/usr/bin/python3
"""
Function that adds two numbers and prints the result.

"""


def add_integer(a, b=98):
    """
    Checks if a and b are either int or
    float data type, if not, throw an error.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    """
    Casts a and b into int data type, just in case they're floats.

    """
    a = int(a)
    b = int(b)

    """
    Returns the value of the addition of a and b.

    """
    return (a + b)
