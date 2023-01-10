#!/usr/bin/python3
'''Function that creates an Object from a “JSON file”.'''
import json


def load_from_json_file(filename):
    '''
    Function that creates an Object from.
    A “JSON file” using the with statement.'''

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
