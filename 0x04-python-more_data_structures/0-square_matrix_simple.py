#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda ele: list(map(lambda x: x ** 2, ele)), matrix))
