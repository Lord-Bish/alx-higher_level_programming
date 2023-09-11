#!/usr/bin/python3
"""This module creates a class rectangle"""
class Rectangle:
    """a rectangle class"""
    def __init__(self, width=0, height=0):
        """
        Constructor of the class Rectangle
          Args:
            - width (default = 0): int
            - heigth (default = 0): int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """a getter method"""
        return (self.__width)

    @width_setter
    def width(self, value):
        """
        a setter method of with attribute
          Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """a getter method"""
        return (self.__height)

    @height_setter
    def height(self, value):
        """
        a setter of the height attribute
          Args:
            - value: int
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


