#!/usr/bin/python3

def weight_average(my_list=[]):
    '''function that returns the weighted average of all
    integers tuple (<score>, <weight>)'''
    if not my_list:
        return 0

    numbr = 0
    denom = 0

    for tup in my_list:
        numbr += tup[0] * tup[1]
        denom += tup[1]

    return (numbr / denom)
