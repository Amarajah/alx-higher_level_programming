#!/usr/bin/python3

def safe_print_integer(value):
    return False
    try:
        print("{:d}".format(value))
        result = True
    except Exception:
        result = False
    return (result)
