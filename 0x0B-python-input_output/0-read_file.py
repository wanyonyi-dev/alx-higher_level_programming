#!/usr/bin/python3
"""Reads files"""


def read_file(filename=""):
    """Reads a file and prints its content"""
    with open(filename, encoding="utf-8") as txt_file:
        print(txt_file.read(), end="")
