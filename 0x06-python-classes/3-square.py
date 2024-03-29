#!/usr/bin/python3
"""
This module creates a class called square with a private size attribute
"""
class Square:
    """The square class"""
    def __init__(self, size=0):
        """initializing the size attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A public method of the class square"""
        return (self.__size * self.__size)
