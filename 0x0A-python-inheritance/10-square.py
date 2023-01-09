#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Representation of a square.'''

    def __init__(self, size):
        '''Initialization of the function.'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
