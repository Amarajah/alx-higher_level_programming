#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    if isinstance(x, int):
        print("{:d}".format(x), end=" ")

    try:
        print("{:d}".format(x), end=" ")
    except IndexError:
        print("Index out of range")
