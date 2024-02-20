#!/usr/bin/python3
"""JSON string"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    Args:
        my_obj: dict
    """
    return json.dumps(my_obj)

