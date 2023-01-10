#!/usr/bin/python3
'''Function that reads a text file (UTF8) and prints it to stdout.'''


def read_file(filename=""):
    '''Opens and reads file using with statement.'''
    with open("", encoding="utf-8") as f:
        read_data = f.read()
