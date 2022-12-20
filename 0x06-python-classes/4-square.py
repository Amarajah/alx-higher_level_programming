#!/usr/bin/python3


"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """ Sets the size attribute."""
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):

        """Check if size is an integer."""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        """Check if size is less than 0."""

        if size < 0:
            raise ValueError('size must be > 0')
