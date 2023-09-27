#!/usr/bin/python3
"""
This module creates a function that appends text in a file
"""

def append_write(filename="", text=""):
    """this function appends a text to a file"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
