#!/usr/bin/python3

def number_keys(a_dictionary):
    '''function that returns the number of keys in a dictionary.'''
    numbr = 0
    keys_dict = list(a_dictionary.keys())

    for i in keys_dict:
        numbr += 1

    return (numbr)
