#!/usr/bin/python3
""" This module creates a function that prints a square using # """

def print_square(size):
    """ A function that prints a square using #
        size is the length of the square to be printed 
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
   
    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size, sep="")
