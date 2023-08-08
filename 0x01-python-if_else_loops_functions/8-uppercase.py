#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
"""Print string in uppercase."""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - ord('a') + ord('A'))
        print("{}".format(c), end="")
    print("")
