#!/usr/bin/python3


"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """ Sets the size attribute."""
        self.size = size
        self.position = position

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
                print("#" * self.size)

    @property
    def position(self):
        """Returns position of object."""

        return self._position

    @position.setter
    def position(self, value):
        """Checks if position is a tuple of two positive integers."""

        if type(value) != tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Gets the area of the square."""

        return (self._size * self._size)

    def my_print(self):
        """Prints in stdout the square with the character #."""

        if self.size == 0:
            print(" ")  # print an empty line
        else:
            for i in range(self.size):
                for line in range(self.position[1]):
                    print(" ")
            for i in range(self.__size):
                for space in range(self.position[0]):
                    print(" ", end=" ")
                for j in range(self.size):
                    print('#', end=" ")
                print(" ")
