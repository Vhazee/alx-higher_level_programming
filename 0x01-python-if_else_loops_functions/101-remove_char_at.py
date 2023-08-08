#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(str, n):
"""Create a copy of string withoutcharacter at position n."""
    if n < 0 or n >= len(str):
        return (str)
    return (str[:n] + str[n+1:])
