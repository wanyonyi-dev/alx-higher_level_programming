#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file

    Args:
      filename: text filename (str)
    """
    with open(filename, mode="r", encoding="utf-8") as txt_file:
        return json.loads(txt_file.read())

