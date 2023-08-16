#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''function that adds all unique integers in a list (only once for each integer).'''
    unique_list = set(my_list)
    numbr = 0

    for i in unique_list:
        numbr += i

    return (numbr)
