#!/usr/bin/python3
"""This module creates a class that rebels"""

class MyInt(int):
    """a class that inherites from a base class"""

    def __eq__(self, other):
        """invertes the == operator"""

        return (int(self) != int(other))

    def __ne__(self, other):
        """invertes the != operator"""

        return (int(self) == int(other))
