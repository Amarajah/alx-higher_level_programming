#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except TypeError, ZeroDivisionError:
        result = None
    finally:
        print("{:d} / {:d} = {}".format(a, b, result), end=" ")
    return (result)
