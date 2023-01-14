#!/usr/bin/python3
"""Defines a class Rectangle."""
"""Taking width and height as private attributes."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):

        """
        Sets the width and height attributes.

        Args:
        width (int): width of new rectangle.
        height (int): height of new rectangle.

        """

        self.width = width
        self.height = height

    @property
    def width(self):

        """Returns value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for private attribute width.
        Value(int) new width value.
        """

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
        """
        Setter function for private attribute height.
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
