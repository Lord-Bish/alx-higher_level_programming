#!/usr/bin/python3
"""" This module creates a function that adds two integers together and return their result """
def add_integer(a, b=98):
    """ This function adds two integers together """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    a = int(a)

    if not isinstance(b, int) and not isinstance(b float):
        raise TypeError("b must be an integer")
    b = int(b)

    return (a + b)
