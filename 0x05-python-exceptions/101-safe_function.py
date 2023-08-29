#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    You can assume fct will be always a pointer to a function
    Returns the result of the function,
    Otherwise, returns None if something happens during the
    function and prints in stderr the error precede by Exception:
    You have to use try: / except:
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
