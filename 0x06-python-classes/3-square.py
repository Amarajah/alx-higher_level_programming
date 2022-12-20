#!/usr/bin/python3


"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """ Sets the size attribute."""

        """Check if size is an integer."""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        """Check if size is less than 0."""

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Gets the area of the square."""
    return self * self
