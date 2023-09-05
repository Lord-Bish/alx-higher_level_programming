#!/usr/bin/python3
"""This module creates a class called square"""
class Square:
    """The square class"""
    def __init__(self, size=0):
        """initializimg the size attribute"""
        self.size = size

    @property
    def size(self):
        """setting a property getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """define a property setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__value = value

    def area(self):
        """Returns the area of a square"""
        return (self.__size * self.__size)
