#!/usr/bin/python3
"""This module creates a function that reads a file"""

def read_file(filename=""):
    """function that reads a file"""

    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
