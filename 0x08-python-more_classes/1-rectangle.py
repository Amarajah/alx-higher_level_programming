#!/usr/bin/python3

"""Defines a class Rectangle."""


class Rectangle:

    """Represents a rectangle."""

    def __init__(self, width=0, height=0):

        """ Sets the width and height attributes."""
        self.__width = width
        self.__height = height

    def width(self, value):

        """Defines the width attribute, and checks its an integer."""

        """If its not an int/less than 0, raise error."""

    if not isinstance(width, int):
        raise TypeError('width must be an integer')

    if width < 0:
        raise ValueError('width must be >= 0')

    self.__width = width

    def height(self, value):

        """Defines height attribute,and checks its an  integer."""

        """If its not an int/less than 0, raise error."""

        if not isinstance(height, int):
            raise TypeError('height must be an integer')

        if height < 0:
            raise ValueError('heightmust be >= 0')

        self.__height = height
