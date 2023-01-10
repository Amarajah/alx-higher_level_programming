#!/usr/bin/python3
'''A function to illustrate the file-append function.'''


def append_write(filename="", text=""):
    '''Write the function using the with statement.'''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
