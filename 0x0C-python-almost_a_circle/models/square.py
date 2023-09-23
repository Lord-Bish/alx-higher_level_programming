#!/usr/bin/python3
"""This module creates a class with inheritance"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """a Square with rectangle inheritance"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """a string representation"""

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    @property
    def size(self):
        """a size getter method"""

        return (self.width)

    @size.setter
    def size(self, value):
        """a size setter method"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates attributes"""

        if args is not None and len(args) is not 0:
            list_args = ["id", "size", "x", "y"]

            for i in range(len(args)):
                if list_args[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, list_args[i], args[i])

        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        returns dictionary representation of a Square
        """

        dict_atr = ["id", "size", "x", "y"]

        dict_data = {}

        for key in dict_atr:
            if key == "size":
                dict_data[key] = getattr(self, width)
            else:
                dict_data[key] = getattr(self, key)

        return (dict_data)
