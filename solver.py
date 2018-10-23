import argparse

from utils import matmul, transpose


# TODO:
# * Write CGM

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
    content = [x.strip() for x in content]

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
    return 0


def solve(filename):
    """
    Solves the system.
    :param filename: string - path to file with data
    :return: (list [dim, 1]) - solution to the system
    """
    dim, eps, A, b = process_data(filename)
    b = matmul(transpose(A), b)
    A = matmul(transpose(A), A)
    return сonjugate_gradient_method(dim, eps, A, b)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store')
    args = parser.parse_args()

    x = solve(args.file)
