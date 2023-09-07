#!/usr/bin/python3
""" This module creates a class rectangle """
class Rectangle:
    """ a rectangle class """
    def __init__(self, width=0, height=0):
        """ initializes class instances """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ a getter method """
        return (self.__width)

    @width_setter
    def width(self, value):
        """ a setter method """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ a getter method """
        return (self.__height)

    @height_setter
    def height(self, value):
        """ a setter method """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


