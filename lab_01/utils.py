from math import sqrt


def matrix_multiplication(lhs, rhs):
    """
    Unsafe matrix multiplication. If params are incorrect, behavior is undefined.
    :param lhs: list [m, n] - first matrix
    :param rhs: list [n, l] - second matrix
    :return: matrix (list [m, l]) - multiplication of lhs and rhs
    """
    matrix = []
    for i in range(len(lhs)):
        row = []
        for j in range(len(rhs[0])):
            value = 0
            for k in range(len(rhs)):
                value += lhs[i][k] * rhs[k][j]
            row.append(value)
        matrix.append(row)
    return matrix


def matrix_transpose(matrix):
    """
    Unsafe matrix transposition. If params are incorrect, behavior is undefined.
    :param matrix: list [m, n] - given matrix
    :return: transposed_matrix (list [n, m]) - transposition of the given matrix
    """
    transposed_matrix = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transposed_matrix.append(row)
    return transposed_matrix


def matrix_subtraction(lhs, rhs):
    """
    Unsafe matrix subtraction. If params are incorrect, behavior is undefined.
    :param lhs: list [m, n] - first matrix
    :param rhs: list [m, n] - second matrix
    :return: matrix (list [m, n]) - subtraction of lhs and rhs
    """
    matrix = []
    for i in range(len(lhs)):
        row = []
        for j in range(len(lhs[0])):
            row.append(lhs[i][j] - rhs[i][j])
        matrix.append(row)
    return matrix


def matrix_addition(lhs, rhs):
    """
    Unsafe matrix addition. If params are incorrect, behavior is undefined.
    :param lhs: list [m, n] - first matrix
    :param rhs: list [m, n] - second matrix
    :return: matrix (list [m, n]) - sum of lhs and rhs
    """
    matrix = []
    for i in range(len(lhs)):
        row = []
        for j in range(len(lhs[0])):
            row.append(lhs[i][j] + rhs[i][j])
        matrix.append(row)
    return matrix


def matrix_scalar_multiplication(matrix, scalar):
    """
    Unsafe matrix multiplication by scalar. If params are incorrect, behavior is undefined.
    :param matrix: list [m, n] - matrix
    :param scalar: float - scale coefficient
    :return: new_matrix (list [m, n]) - scaled matrix
    """
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[i][j] * scalar)
        new_matrix.append(row)
    return new_matrix


def matrix_cross_product(lhs, rhs):
    """
    Unsafe matrix cross product. If params are incorrect, behavior is undefined.
    :param lhs: list [m, 1] - first matrix
    :param rhs: list [m, 1] - first matrix
    :return: value (float) - cross product of lhs and rhs
    """
    value = 0
    for i in range(len(lhs)):
        value += lhs[i][0] * rhs[i][0]
    return value


def dist(lhs, rhs):
    """
    Unsafe distance calculation. If params are incorrect, behavior is undefined.
    :param lhs: list [m, 1] - first matrix
    :param rhs: list [m, 1] - first matrix
    :return: value (float) - distance between lhs and rhs
    """
    value = 0
    _ = matrix_subtraction(lhs, rhs)
    for i in range(len(lhs)):
        value += _[i][0] * _[i][0]
    return sqrt(value)
