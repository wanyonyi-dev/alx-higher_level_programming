#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """
    Append s string to the end of a text file.
    If file do not exist - it creates it

    Args:
        filename: string
        text: string
    Returns: the number of characters added (int)
    """
    with open(filename, mode="a", encoding="utf-8") as txt_file:
        return txt_file.write(text)
