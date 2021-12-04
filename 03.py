import numpy as np


def get_data():
    data = []
    with open("data/03.txt", "r") as file:
        for row in file:
            row = row.strip()
            row_data = np.zeros(len(row), dtype=int)
            for i, entry in enumerate(row):
                row_data[i] = int(entry)
            data.append(row_data)
    data = np.array(data)
    return data


def conversion(np_array):
    out = 0
    for power, entry in enumerate(reversed(np_array)):
        if entry:
            out += 2**power
    return out

def first_solution(data):
    count = np.sum(data, axis=0)
    gamma = count > 500
    eps = 1 - gamma
    print("gamma", gamma,  conversion(gamma))
    print("eps", eps, conversion(eps))
    print("power", conversion(gamma) * conversion(eps) )

def filtering_ox(data, bit):
    count = np.sum(data[:, bit])
    if count >= (data.shape[0]/2.):
        selection = 1
    else:
        selection = 0
    idx = data[:, bit] == selection
    return data[idx]



def filtering_co2(data, bit):
    count = np.sum(data[:, bit])
    if count < (data.shape[0]/2.):
        selection = 1
    else:
        selection = 0
    idx = data[:, bit ] == selection
    return data[idx]


def second_solution(data):
    data_ox = data.copy()
    for bit in range(data.shape[1]):
        data_ox = filtering_ox(data_ox, bit)
        if len(data_ox) == 1:
            break

    data_co2 = data.copy()
    for bit in range(data.shape[1]):
        data_co2 = filtering_co2(data_co2, bit)
        if len(data_co2) == 1:
            break

    print(f"co2: {data_co2[0]}, {conversion(data_co2[0])}")
    print(f"oxygen: {data_ox[0]}, {conversion(data_ox[0])}")
    print(f"Result: {conversion(data_co2[0]) * conversion(data_ox[0])}")


if __name__ == "__main__":
    data = get_data()
    first_solution(data)
    second_solution(data)