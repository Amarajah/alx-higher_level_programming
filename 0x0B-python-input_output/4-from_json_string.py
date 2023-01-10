#!/usr/bin/python3
'''
Function that returns an object (Python data structure).
Represented by a JSON string.
'''
import json


def from_json_string(my_str):
    '''Function to illustrate the first writeup.'''
    return json.loads(my_str)
