#!/usr/bin/python3
"""
This program have an incompleted class
"""

prevRectangle = __import__(8-rectangle.py).Rectangle

class Rectangle(prevRectangle):
    """a class that inherites from the base class"""

    def __init__(self, width, height):
        """initializes class attributes"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area"""
        self.__width * self.__height

    def __str__(self):
        """returns string representation"""
        return ("[Rectangle]{:d}/{:d}".format(self.__width, self.__height))
