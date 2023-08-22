#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == 0:
        return (my_list)

    new_list = [elem for elem != search else replace for elem in my_list]
    return (new_list)
