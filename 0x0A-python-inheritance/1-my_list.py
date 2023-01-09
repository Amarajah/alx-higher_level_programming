#!/usr/bin/python3

'''A class MyList that inherits from list.'''


class MyList(list):
    '''Method to print list in ascending order.'''

    def print_sorted(self):
        '''Sort and return list.'''

        print(sorted(self))
