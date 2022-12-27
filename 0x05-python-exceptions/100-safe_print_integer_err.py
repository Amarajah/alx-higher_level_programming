#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end=" ")
        return (True)
    except TypeError, ValueError:
        print("Exception: {} is not an integer".format(value), file=sys.stderr)
        return (False)
