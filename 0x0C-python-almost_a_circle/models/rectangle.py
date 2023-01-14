#!/usr/bin/python3
'''
This class inherits from Base.
'''
from models.base import Base


class Rectangle:
    '''
    Private instance attributes, each with its own public getter and setter.
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialization.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Returns value of width.'''
        self.__width = width

    @property
    def height(self):
        '''Returns value of height.'''
        self.__height = height

    @property
    def x(self):
        '''Returns value of x.'''
        self.__x = x

    @property
    def y(self):
        '''Returns value of y.'''
        self.__y = y


    @width.setter
    def width(self, value):
        '''Ensuring width is an int.'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @height.setter
    def height(self, value):
        '''Ensuring height is an int.'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @x.setter
    def x(self, value):
        '''Ensuring x is an int.'''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @y.setter
    def y(self, value):
        '''Ensures y is a valid int.'''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')

    def area(self):
        '''Defines the area of the rectangle.'''
        return (self.__width * self__height)

    def display(self):
        '''
        Prints in stdout the Rectangle instance with the character #.
        '''
        if self.__height or self.__width == 0:
            return ('')

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
            return ("".join(rect))
