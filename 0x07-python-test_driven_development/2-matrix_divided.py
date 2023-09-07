#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ Divide a matrix by a number div """
    list_error = "matrix should be a matrix (list of lists) of integers/floats"
    len_error = "Each row of the matrix should have the same size"
    div_int_error = "div should be a number"
    div_zero_error = "division by zero"
    new_matrix = []
    new_list = []
    if not matrix:
        raise TypeError(list_error)
    if type(div) is not int and type(div) is not float:
        raise TypeError(div_int_error)
    if div is 0:
        raise ZeroDivisionError(div_zero_error)
    longitud = len(matrix[0])
    for lista in matrix:
        if type(lista) is not list:
            raise TypeError(list_error)
        if len(lista) != longitud:
            raise TypeError(len_error)
        for item in lista:
            if type(item) is not int and type(item) is not float:
                raise TypeError(list_error)
            num = item / div
            new_list.append(round(num, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
