def matmul(lhs, rhs):
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


def transpose(matrix):
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
