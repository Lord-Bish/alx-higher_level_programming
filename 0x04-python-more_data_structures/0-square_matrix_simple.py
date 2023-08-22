#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []

    if new_list == 0:
        return (new_list)

    new_list = [[i*i for i in j] for j in matrix]
    return (new_list)
