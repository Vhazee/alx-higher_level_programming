#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list."""
    mltpls_of_two = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mltpls_of_two.append(True)
        else:
            mltpls_of_two.append(False)
    return (mltpls_of_two)
