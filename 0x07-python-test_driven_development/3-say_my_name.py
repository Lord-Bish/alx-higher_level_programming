#!/usr/bin/python3
""" This module creates a function that says someone's name """

def say_my_name(first_name, last_name=""):
    """ A function that says a name
        
        first_name and last_name must be a string
        otherwise, raise a TypeError withe a message
        "first_name or last_name must be a string"

        prints "my name is {first_name last_nmae}"
    """

    if not isinstance(first_name, str):
        raise TypeError("First_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("Last_name must be a string")

    print(f"My name is {first_name} {last_name}")
