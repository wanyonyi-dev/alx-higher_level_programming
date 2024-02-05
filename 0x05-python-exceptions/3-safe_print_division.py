#!/usr/bin/python3
def safe_print_division(a, b):
    Qu = 0
    try:
        qu = a / b
    except ZeroDivisionError:
        qu = None
    finally:
        print("Inside result: {}".format(qu))
    return qu

