#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print x elememts of a list.
    my_list can contain any type (integer, string, etc.)
    All elements must be printed on the same line followed by a new line.
    x represents the number of elements to print
    x can be bigger than the length of my_list
    Returns the real number of elements printed
    You have to use try: / except:
    You are not allowed to import any module
    You are not allowed to use len()
    """
    retn = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            retn += 1
        except IndexError:
            break
    print("")
    return (retn)
