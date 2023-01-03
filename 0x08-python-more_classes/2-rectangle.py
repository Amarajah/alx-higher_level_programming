#!/usr/bin/python3

"""Defines a class Rectangle."""


class Rectangle:

    """Represents a rectangle."""

    def __init__(self, width=0, height=0):

        """ Sets the width and height attributes."""
        self.width = width
        self.height = height

    @property
    def width(self):

        """Returns value of width."""
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

    self.__width = value

    @property
    def height(self):
        """Returns value of height."""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('heightmust be >= 0')

        self.__height = value

    def area(self):
        """Returns rect area."""
        return (self.__width * self.__height)

    def perimeter(self): 
        """Returns rect area."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
