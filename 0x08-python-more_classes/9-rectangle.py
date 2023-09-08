#!/usr/bin/python3
"""This module creates a class rectangle"""
class Rectangle():
    """a rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes class instances"""
        self.width = width
        self.height = height

        number_of_instances += 1

    def __str__(self):
        """prints string format"""
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        else:
            for i in range(0, self.__height):
                print(print_symbol * self.__width)

    def __repr__(self):
        """prints string representation"""
        return (f"Rectangle("{self.__width}"," {self.__height}")")

    def __del__(self):
        """calls when class instance is deleted"""
        print("Bye rectangle...")

        number_of_instances -= 1

    @property
    def width(self):
        """a getter method"""
        return (self.__width)

    @width_setter
    def width(self, value):
        """a setter method"""
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
        """a setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """prints area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """prints perimeter"""
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """prints rectangle with bigger area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (Rectangle.area(rect_1) >= Rectangle.area(rect_2)):
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """returns a square instance"""
        return (cls(size, size))

