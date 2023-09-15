#!/usr/bin/python3
"""
This module creates a function that checkes for subclasses
"""

def inherits_from(obj, a_class):
    """checkes for subclasses"""

    if type(obj) == a_class:
        return (False)

    return (isinstance(obj, a_class))
