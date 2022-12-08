#!/usr/bin/python30
def uniq_add(my_list=[]):
    unique = []
    for number in my_list:
        if number not in unique:
            unique.append(number)
   result =  sum(set(unique))
   return result
