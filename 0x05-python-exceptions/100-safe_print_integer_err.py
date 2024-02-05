#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as err:
        print("Exeption: {}".format(err), file = sys.stderr)
        return False
    except ValueError as err:
        print("Exeption: {}".format(err), file = sys.stderr)
        return False

