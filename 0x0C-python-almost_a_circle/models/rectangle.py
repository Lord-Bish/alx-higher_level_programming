#!/usr/bin/python3
"""
This module creates a new class that inherites from base class
"""

from models.base import Base

class Rectangle(Base):
    """a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class instance constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) != int:
            raise TypeError(f"width must be an integer")

        if value < 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """a height getter method"""

        return self.__height

    @height.setter
    def height(self, value):
        """a height setter method"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """an x getter method"""

        return self.__x

    @x.setter
    def x(self, value):
        """an x setter method"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """a y getter method"""

        return self.__y

    @y.setter
    def y(self, value):
        """a y setter method"""

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """returns the area of the rectangle"""

        return (self.width * self.height)

    def display(self):
        """prints rectangle with #"""

        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end="")

    def __str__(self):
        """string representation"""

        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """updates methods"""

        if args is not None and len(args) is not 0:
            list_attr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])

        else:
            for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        returns dictionary representation of rectangle
        """

        dict_attr = ["id", "width", "height", "x", "y"]

        dict_data = {}

        for key in dict_attr:
            dict_data[key] = getattr(self, key)

        return (dict_data)
