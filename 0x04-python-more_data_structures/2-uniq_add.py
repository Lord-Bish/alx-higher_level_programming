#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)

    num = 0

    for i in my_list:
        num += i
    return (num)
