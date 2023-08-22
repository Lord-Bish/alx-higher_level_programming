#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()

    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        new_dict *= 2

    return (new_dict)
