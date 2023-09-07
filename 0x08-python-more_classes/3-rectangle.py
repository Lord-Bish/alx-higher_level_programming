#!/usr/bin/python3
""" This module creates a class rectangle """
class Rectangle:
    """ a rectangle class """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def __str__(self):
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        else:
            for i in range(0, self.__height):
                print("#" * self.__width)
            print()

    @property
    def width(self):
        return (self.__width)

    @width_setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height_setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))
