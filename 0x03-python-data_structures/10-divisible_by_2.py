#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy = my_list.copy()
    for i in range(len(copy)):
        if copy[i] % 2 == 0:
            return True
        else:
            return False
    return copy
