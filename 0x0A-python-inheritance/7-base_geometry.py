#!/usr/bin/python3
"""
This program have an incompleted class
"""


class BaseGeometry():
    """
    This class contain a method not implemented
    """

    def area(self):
        """
        This function raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value type"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
