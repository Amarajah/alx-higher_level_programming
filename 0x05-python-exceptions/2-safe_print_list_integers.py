#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for count in range(x):
        try:
            print("{:d}".format(my_list[count]))
            count += 1
        except (TypeError, IndexError):
            pass
    print(" ")
    return count
