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

    def __str__(self):
        """ change str representantion when print object """
        id_str = str(self.id)
        w_str = str(self.__width)
        h_str = str(self.__height)
        x_str = str(self.__x)
        y_str = str(self.__y)
        div_str = x_str + '/' + y_str + ' - ' + w_str + '/' + h_str
        return ("[Rectangle] " + '(' + id_str + ') ' + div_str)

    def update(self, *args, **kwargs):
        '''Update id, width, height, x and y, this order.'''
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x == value
                elif key == "y":
                    self.y == value
    def to_dictionary(self):
        ''' Returns dict representation of rectangle.'''
        i = self.id
        w = self.width
        h = self.height
        x = self.x
        y = self.y

        dict = {'id' : i, 'width' : w, 'height' : h, 'x' : x, 'y' : y}
        return (dict)
