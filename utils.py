import numpy as np

def import_to_numpy(file):
    return np.loadtxt(file)


def to_number(binary):
    """

    :param binary: list of 0s and 1s
    :return: int that is that number
    """
    out = 0
    for i, value in enumerate(reversed(binary)):
        out += value * 2**i
    return out