#!/usr/bin/python3
""" This module creates a class rectangle """
class Rectangle:
    """ a rectangle class """
    def __init__(self, width=0, height=0):
        """ initializes class instances """
        self.width = width
        self.height = height
    
    def __str__(self):
        """ prints string format """
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        else:
            for i in range(0, self.__height):
                print("#" * self.__width)
            print()
    
    def __repr__(self):
        """ prints the string representation """
        return (f"Rectangle("{self.__width}"," {self.__height}")")

    @property
    def width(self):
        """ a getter method """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ a setter function """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ a getter function """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ a setter method """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ returns the area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the perimeter """
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))
