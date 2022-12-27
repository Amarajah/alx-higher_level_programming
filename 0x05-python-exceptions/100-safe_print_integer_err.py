#!/usr/bin/python3


def safe_print_integer_err(value):
    if isinstance(value, int):
        return True
    else:
        return False

    try:
        print("{:d}".format(value), end=" ")
    except TypeError:
        print("Exception: {} is not an integer".format(value))
