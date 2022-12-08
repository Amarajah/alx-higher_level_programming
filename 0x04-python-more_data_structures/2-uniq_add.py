#!/usr/bin/python30
def uniq_add(my_list=[]):
    unique = []
    result = sum(set(unique))
    for number in my_list:
        if number not in unique:
            unique.append(number)
   return result
