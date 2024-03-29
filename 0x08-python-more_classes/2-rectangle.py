#!/usr/bin/python3
"""This module creates a class rectangle"""

class Rectangle():
    """
    A rectangle class with private instance attributes
    """

    def __init__(self, width=0, height=0):
        """
        This method initializes class attributes
        args:
            - width (default = 0): int
            - height (default = 0): int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """a getter method"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        a setter method
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

    @height.setter
    def height(self, value):
        """
        A setter method
          Args:
              - value: int
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter"""
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))
