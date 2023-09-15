#!/usr/bin/python3
"""This module creates a class with inheritance"""

class MyList(list):
    """This class inherites from a base class"""

    def print_sorted(self):
        """prints a sorted list"""

        print(sorted(self))
