#!/usr/bin/python3
"""
Module 0-lookup
Finding a list of available attributes & methods of an object
"""


def lookup(obj):
    """
    This function returns a list of attributes and methods in and object
    Args:
        obj: The object to be looked into
    """
    return dir(obj)

