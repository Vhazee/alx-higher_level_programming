#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Removes all characters c and C from string."""
    my_copy = [s for s in my_string if s != 'c' and s != 'C']
    return ("".join(my_copy))
