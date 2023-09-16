#!/usr/bin/python3
"""
This program create a Square from a Rectangle
"""


prevSquare = __import__('10-square.py').Square


class Square(prevSquare):
    """Class Squared based from Rectangle"""
    def __init__(self, size):
        """Constructor of Square"""

        super.__init__(size)


    def __str__(self):
        """returns the string representation"""
        return ("[Square] {0:d}/{0:d}".format(self.__size))
