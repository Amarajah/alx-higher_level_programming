#!/usr/bin/python3
'''Function to chck that obj is in designated class.'''


def is_same_class(obj, a_class):
    '''Return true or false.'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
