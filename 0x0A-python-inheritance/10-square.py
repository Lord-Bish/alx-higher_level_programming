#!/usr/bin/python3
"""
This program use the inherit for create a new Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """a square class that inherites from base class"""

    def __init__(self, size):
        """Initializes the size attribute"""

        self.integer_validator("size", size)
        self.__size = size
        super.__init__(size, size)

    def area(self):
        """returns the area"""
        return (self.__size **2)
