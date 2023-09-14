#!/usr/bin/python3
#0-square_matrix_simple.py
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    return list(list(map(lambda x: x*x, row)) for row in matrix)
