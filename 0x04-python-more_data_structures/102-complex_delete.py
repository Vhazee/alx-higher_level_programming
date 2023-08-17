#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    '''function that deletes keys with a specific value in a dictionary.'''
    key_list = list(a_dictionary.keys())

    for value_dict in key_list:
        if value == a_dictionary.get(value_dict):
            del a_dictionary[value_dict]

    return (a_dictionary)
