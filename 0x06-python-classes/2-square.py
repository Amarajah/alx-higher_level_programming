#!/usr/bin/python3


"""Define a class Square."""



class Square:

    """Represent a square."""

    def __init__(self, size=0):
        """ Sets the size attribute."""
        self.__size = size

        """Create an instance of the Square class with a size of 5."""
        s1 = Square(5)
        print(f'The square has a size of {s1._Square.__size}')

        """Try creating a square with size 'a'(TypeError)."""
        try:
            s1 = Square('a')
        except TypeError:
            print('size must be an integer')

        """Try creating a square  with aless than 0 value(ValueError)."""
        try:
            s2 = Square(-1)
        except ValueError:
            print('size must be >= 0')
