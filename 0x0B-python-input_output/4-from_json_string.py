#!/usr/bin/python3
"""JSON string to Object"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string
    Args:
        my_str: the given string
    """
    return json.loads(my_str)

