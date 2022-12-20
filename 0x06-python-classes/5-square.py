#!/usr/bin/python3


"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """ Sets the size attribute."""
        self.size = size

    @property
    def size(self):
        """Returns value of size."""
        return self._size

    @size.setter
    def size(self, value):

        """Check if size is an integer."""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        """Check if size is less than 0."""

        if value < 0:
            raise ValueError('size must be > 0')

        self._size = value

    def area(self):
        """Returns area of square."""
        return (self._size * self._size)

    def my_print(self):
        """Prints in stdout the square with the character #."""

        if self.size == 0:
            print(" ")  # print an empty line

        else:
            for i in range(self.size):
                print("#" *self.size)
