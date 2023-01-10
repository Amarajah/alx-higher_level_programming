#!/usr/bin/python3

'''
Function that writes a string to a text file.
And returns the number of characters written.
'''


def write_file(filename="", text=""):
    '''Function that writes a string to a text file using with.'''
    with open(filename, encoding="utf-8") as f:
        print(f.write(), end="")
