#!/usr/bin/python3
'''
Base of all other classes in this project.
'''


class Base:
    __nb_objects = 0

    '''
    The goal of this is to manage id attribute in all future classes.
    And to avoid duplicating the same code (by extension, same bugs).
    Private class attribute:__nb_object (int): Number of instantiated Bases.
    '''

    def __init__(self, id=None):
        '''Init function.'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
