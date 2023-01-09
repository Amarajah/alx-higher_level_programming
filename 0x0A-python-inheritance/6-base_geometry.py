#!/usr/bin/python3
'''Creates an empty class.'''


class BaseGeometry:
    '''Represent base geometry.'''

    def area(self):
        '''Area of the shape.'''
        raise Exception("area() is not implemented")
