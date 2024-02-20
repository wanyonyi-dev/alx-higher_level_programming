#!/usr/bin/python3
"""Save Object to af file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file

    Args:
        my_obj: the object (obj)
        filename: the text file (str)
    """
    with open(filename, mode="w", encoding="utf-8") as txt_file:
        txt_file.write(json.dumps(my_obj))

