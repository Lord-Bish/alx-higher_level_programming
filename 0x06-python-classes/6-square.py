#!/usr/bin/python3
"""This module creates a square class"""
class Square:
    """a square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initializing instance attributes"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """setting a getter method to access the attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """creating a setter function for size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """private instance of square class"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """creating a setter method for the attribute"""
        if (not isinstance(value, tuple)) or (len(value) != 2) or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """prints the area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints a square with a # symbol"""
        if self.__size == 0:
            print("--")
            return

        for i in range(0, self.__position[1]):
            print("--")

        for i in range(0, self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")
