#!/usr/bin/python3
"""
This module creates a function that adds attributes if possible
"""


def add_attribute(obj, name, value):
    """Method for checking and adding new attribute"""

    if hasattr(obj, "__dict__") or \
       (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
