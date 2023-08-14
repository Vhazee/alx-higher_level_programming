#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replaces an element in the copied list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    my_copy = [s for s in my_list]
    my_copy[idx] = element
    return (my_copy)
