#!/usr/bin/python3
"""
This module creates a function that assert instance of classes
"""

def is_same_class(obj, a_class):
    """Checks if obj is a class instance"""
    return (type(obj) == a_class)
