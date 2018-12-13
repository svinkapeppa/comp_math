from cmath import exp
from math import ceil, log2, pi


def zeros(size):
    """
    Creates list of given size with all zeros
    :param size: int
    :return: list
    """
    return [0] * size


def scale_list(data, factor):
    """
    Scales list in factor times
    :param data: list
    :param factor: number (not 0)
    :return: list
    """
    assert factor != 0, 'ERROR: Zero-division encountered'
    return [item / factor for item in data]


def elementwise_product(lhs, rhs):
    """
    Computes element-wise product of two lists
    :param lhs: list
    :param rhs: list
    :return: list
    """
    assert len(lhs) == len(rhs), 'ERROR: Wrong shapes of operands'
    return [lhs[i] * rhs[i] for i in range(len(lhs))]


def power(base, exponents):
    """
    Exponentiation of number into all elements of list
    :param base: number
    :param exponents: list
    :return: list
    """
    return [base ** exponent for exponent in exponents]


def exponentiation(array, exponent):
    """
    Exponentiation of elements of list into exponent
    :param array: list
    :param exponent: number
    :return: list
    """
    return [item ** exponent for item in array]


def divide(base, array):
    """
    Division of base and all elements of list
    :param base: number
    :param array: list
    :return: list
    """
    return [base / item for item in array]


def complex_round(data, precision):
    """
    Rounds real and imaginary parts of complex number
    :param data: list
    :param precision: int
    :return: list
    """
    return [round(item.real, precision) + 1j * round(item.imag, precision) for item in data]


def fft(x):
    """
    Fast Fourier Transform
    Implemented as suggested by Cooley and Tukey in their original paper
    http://www.ams.org/journals/mcom/1965-19-090/S0025-5718-1965-0178586-1/S0025-5718-1965-0178586-1.pdf
    :param x:
    :return:
    """
    if len(x) <= 1:
        return x

    even = fft(x[0::2])
    odd = fft(x[1::2])

    factor = [exp(-2j * pi * k / len(x)) * odd[k] for k in range(len(x) // 2)]

    lhs = [even[k] + factor[k] for k in range(len(x) // 2)]
    rhs = [even[k] - factor[k] for k in range(len(x) // 2)]

    return lhs + rhs


def ifft(x):
    """
    Inverse Fast Fourier Transform
    Done in a similar manner as fft
    :param x: list
    :return: list
    """
    if len(x) <= 1:
        return x

    even = scale_list(ifft(x[0::2]), 2)
    odd = scale_list(ifft(x[1::2]), 2)

    factor = [exp(2j * pi * k / len(x)) * odd[k] for k in range(len(x) // 2)]

    lhs = [even[k] + factor[k] for k in range(len(x) // 2)]
    rhs = [even[k] - factor[k] for k in range(len(x) // 2)]

    return lhs + rhs


def czt(x, precision=None):
    """
    Chirp z-transform algorithm
    Implemented as suggested by Rabiner, Schafer and Rader in their original paper
    https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1162034
    :param precision: int
    :param x: list
    :return: list
    """
    n = len(x)
    w = exp(-2j * pi / n)
    a = 1.0

    m = int(2 ** ceil(log2(2 * n - 1)))

    chirp = power(w, scale_list(exponentiation(list(range(1 - n, n)), 2), 2))
    inverse_chirp = divide(1, chirp[:2 * n - 1]) + zeros(m - (2 * n - 1))

    xp = elementwise_product(elementwise_product(x, power(a, scale_list(list(range(n)), -1))),
                             chirp[n - 1: 2 * n - 1]) + zeros(m - n)
    r = ifft(elementwise_product(fft(xp), fft(inverse_chirp)))
    result = elementwise_product(r[n - 1: 2 * n - 1], chirp[n - 1: 2 * n - 1])

    if precision:
        result = complex_round(result, precision)

    return result
