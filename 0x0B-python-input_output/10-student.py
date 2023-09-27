#!/usr/bin/python3
"""
This module creates a student class w8th public attributes
"""

class Student:
    """a student class with public instance attr"""

    def __init__(self, first_name, last_name, age):
        """initializes instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        returns dictionary representation of a student class
        """

        def to_json(self, attrs=None):
            """ Method that returns directory description """

            obj = self.__dict__.copy()
            if type(attrs) is list:

                for item in attrs:
                    if type(item) is not str:
                        return obj

                    d_list = {}

                for iatr in range(len(attrs)):
                    for satr in obj:
                        if attrs[iatr] == satr:
                            d_list[satr] = obj[satr]
                    return d_list

                return obj

