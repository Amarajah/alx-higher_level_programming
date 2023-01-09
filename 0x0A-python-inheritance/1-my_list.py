#!/usr/bin/python3

'''A class MyList that inherits from list.'''


class MyList(list):
    '''Method to print list in ascending order.'''

    def print_sorted(self):
        '''Make a copy of the list,then sort and return it.'''
        sorted_list = self.copy
        sorted_list.sort()

        print(sorted_list)
