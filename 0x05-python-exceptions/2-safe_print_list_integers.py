#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    if isinstance(x, int):
        print("{:d}".format(my_list[i]), end=" ")

    try:
        print("{:d}".format(my_list[i]), end=" ")
    except IndexError:
        print("Index out of range")
