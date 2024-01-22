#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        x = True
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        x = False
    return x
