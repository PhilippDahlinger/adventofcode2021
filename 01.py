import numpy as np
from utils import import_to_numpy

inp = import_to_numpy("data/01.txt")
test_inp = np.array([199,
200,
208,
210,
200,
207,
240,
269,
260,
263])


def get_num_inc(inp):
    return (np.sum(np.diff(inp) > 0))

def second_puzzle(inp):
    counter = 0
    old = np.sum(inp[0:3])
    for i in range(1, inp.shape[0]):
        if i + 3 > inp.shape[0]:
            break
        new = np.sum(inp[i:i+3])
        if new > old:
            counter += 1
        old = new
    return counter


if __name__ == "__main__":
    #print(get_num_inc(inp))
    print(second_puzzle(inp))