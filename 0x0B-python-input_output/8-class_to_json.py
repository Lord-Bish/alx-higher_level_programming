#!/usr/bin/python3
"""This module returns dictionary description"""

def class_to_json(obj):
    """returns dictionary description of obj"""

    result = {}

    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()

    return result

