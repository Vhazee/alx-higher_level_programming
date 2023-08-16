#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''function that prints a dictionary by ordered keys.'''
    list_order = list(a_dictionary.keys())
    list_order.sort()
    for i in list_order:
        print("{}: {}".format(i, a_dictionary.get(i)))

