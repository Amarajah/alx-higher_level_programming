#!/usr/bin/python3

def safe_print_integer(value):
    if not isinstance(value, int):
        return False
    else:
        return True

    try:
        print("{:d}".format(int(value)), end="\n")
    except ValueError:
        print(" ")
