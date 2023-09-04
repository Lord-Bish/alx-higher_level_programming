#!/usr/bin/python3
""" This module creates a function that prints texts """

def text_indentation(text):
    """ A function that prints texts """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)

        s = ""

        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3])
