#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        f_safely = fct(*args)
        return f_safely
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
