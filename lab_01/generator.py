import numpy as np


# TODO:
# * Remove numpy
# * Implement det function

def det(matrix):
    return 1


def check_positiveness(matrix):
    for i in range(matrix.shape[0]):
        if det(matrix[:i, :i]) <= 0:
            return False
    return True


def generate_matrix(dim=50):
    matrix = 20 * np.random.rand(dim, dim) - 10
    matrix = matrix @ matrix.T
    return matrix


def generate(dim=50):
    A = generate_matrix(dim)
    while not check_positiveness(A):
        A = generate_matrix(dim)
    x = 2 * np.random.rand(dim, 1) - 1
    b = A @ x
    return A, b, x


if __name__ == '__main__':
    dim = 50
    eps = 1e-6

    A, b, x = generate(dim)

    with open('example.txt', 'w') as fd:
        fd.write(str(dim) + '\n')
        fd.write(str(eps) + '\n')
        for i in b.reshape(-1):
            fd.write(str(i) + '\n')
        for i in A.reshape(-1)[:-1]:
            fd.write(str(i) + '\n')
        fd.write(str(A.reshape(-1)[-1]))

    with open('answer.txt', 'w') as fd:
        for i in x.reshape(-1)[:-1]:
            fd.write(str(i) + '\n')
        fd.write(str(x.reshape(-1)[-1]))
