#!/usr/bin/python3
'''Creates an empty class.'''


class BaseGeometry:
    '''Represent base geometry.'''

    def __init__(self):
        '''Initialize.'''
        self.area = area

    def area(self):
        '''Area of the shape.'''
        raise Exception("area() is not implemented")
