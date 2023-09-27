#!/usr/bin/python3
"""This module creates a student class"""

class Student:
    """a student class with public instance attr"""

    def __init__(self, first_name, last_name, age):
        """initializes instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns dictionary representation of a student class
        """

        return self.__dict__.copy()

