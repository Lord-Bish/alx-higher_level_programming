#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)

    new_list = my_list[:]

    if idx < 0 or idx > (length - 1):
        return (new_list)
    else:
        new_list[idx] = element

        return (new_list)
