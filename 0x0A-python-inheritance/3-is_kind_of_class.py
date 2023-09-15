#!/usr/bin/python3
"""
This module creates a function that checkes for class or subclass instances
"""

def is_kind_of_class(obj, a_class):
    """
    checkes if obj is a an instance of a class or subclass
    """

    return (isinstance(obj, a_class))
