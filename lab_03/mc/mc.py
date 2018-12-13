import random


class Func:
    value = 4

    @staticmethod
    def func(x):
        return x[0] ** 2 + 2 * x[1] ** 2


def mc(func, num_points=20000):
    """
    Monte Carlo integration
    Implemented as it was described in this lectures
    https://arxiv.org/pdf/hep-ph/0006269.pdf
    :return: number
    """
    value = 0

    for _ in range(num_points):
        point = (random.random(), 4 * random.random())
        value += func.func(point)

    return value * func.value / num_points


if __name__ == '__main__':
    random.seed(42)
    print('VALUE: {}'.format(mc(Func)))
