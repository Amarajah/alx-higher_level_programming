#!/usr/bin/python3
"""Class square that inherits from class Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Initialization from rectangle using super init.
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Class constructor initialization.
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Return width.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Defines values of width/height.'''
        self.width = value
        self.height = value

    def __str__(self):
        '''Redefining string.'''
        id_str = str(self.id)
        w_str = str(self.__width)
        x_str = str(self.__x)
        y_str = str(self.__y)
        div_str = x_str + '/' + y_str + ' - ' + w_str + '/' + h_str
        return ("[Square] " + '(' + id_str + ') ' + div_str)

    def update(self, *args, **kwargs):
        """Update id, width, height, x and y, this order."""
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[1] if len(args) >= 2 else self.height
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return dict representation of a square."""
        i = self.id
        w = self.width
        x = self.x
        y = self.y
        dict = {'id': i, 'size': w, 'x': x, 'y': y}
        return dict
