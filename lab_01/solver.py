import argparse

from lab_01.utils import *


def process_data(filename):
    """
    Reads data from file and constructs objects.
    :param filename: string - path to file with data
    :return:
        dim (int) - dimension size of square matrix
        eps (float) - tolerance level
        A (list [dim, dim]) - square matrix
        b (list [dim, 1]) - right side of the system
    """
    with open(filename, 'r') as fd:
        content = fd.readlines()
    content = [entity.strip() for entity in content]

    dim = int(content[0])
    eps = float(content[1])

    b = []
    for i in range(dim):
        b.append(float(content[i + 2]))

    A = []
    for i in range(dim):
        row = []
        for j in range(dim):
            row.append(float(content[i * dim + j + dim + 2]))
        A.append(row)

    return dim, eps, A, b


def сonjugate_gradient_method(dim, eps, A, b):
    """
    https://en.wikipedia.org/wiki/Conjugate_gradient_method
    :param dim: int - matrix dimension
    :param eps: float - tolerance level
    :param A: list [dim, dim] - positive semi-defined symmetric matrix
    :param b: list [dim, 1] - right side
    :return: x (list [dim, 1]) - solution to the given system
    """
    # Create initial values for x, r and z
    x = []
    for i in range(dim):
        x.append([1])
    r = matrix_subtraction(matrix_multiplication(A, x), b)
    z = matrix_scalar_multiplication(r, -1)

    # Main cycle
    _ = matrix_cross_product(r, r)
    while True:
        Az = matrix_multiplication(A, z)
        alpha = _ / matrix_cross_product(z, Az)
        x_prev = x
        x = matrix_addition(x, matrix_scalar_multiplication(z, alpha))
        r = matrix_addition(r, matrix_scalar_multiplication(Az, alpha))
        __ = matrix_cross_product(r, r)
        beta = __ / _
        _ = __
        # Stopping criterion
        if dist(x, x_prev) < eps and dist(matrix_multiplication(A, x), b) < eps:
            return x
        z = matrix_subtraction(matrix_scalar_multiplication(z, beta), r)


def solve(filename):
    """
    Solves the system.
    :param filename: string - path to file with data
    :return: (list [dim, 1]) - solution to the system
    """
    dim, eps, A, b = process_data(filename)

    # Convert vector to matrix
    _b = []
    for i in range(dim):
        _b.append([b[i]])

    b = matrix_multiplication(matrix_transpose(A), _b)
    A = matrix_multiplication(matrix_transpose(A), A)
    return сonjugate_gradient_method(dim, eps, A, b)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store')
    args = parser.parse_args()

    solution = solve(args.file)
    print(solution)
