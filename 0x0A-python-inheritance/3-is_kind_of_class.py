#!/usr/bin/python3
'''Same class or inherit from.'''


def is_kind_of_class(obj, a_class):
    '''
    Function that returns True if the object is an instance of.
    if the object is an instance of a class that inherited
    from a specific class.
    Else returns false.
    '''

    if isinstance(obj, a_class):
        return True
    return False
