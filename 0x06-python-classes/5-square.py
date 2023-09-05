#!/usr/bin/python3
"""This module creates a class square"""
class Square:
    """a square class"""
    def __init__(self, size=0):
        """initializing the size attribute"""
        self.size = size

    @property
    def size(self):
        """setting a getter function"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """defining setter function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints a square with the # symbol"""
        if self.__size == 0:
            print("--")
        else:
            for i in range(0, self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
