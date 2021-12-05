import numpy as np

def get_data():
    data = []
    for line in open("data/05.txt"):
        line = line.strip()
        a, b = line.split(" -> ")
        a1, a2 = a.split(",")
        b1, b2 = b.split(",")
        data.append([int(a1), int(a2), int(b1), int(b2)])
    return np.array(data)


def solution(data, diagonals=True):
    ocean = np.zeros((1000, 1000), dtype=int)
    for line in data:
        if line[0] != line[2] and line[1] != line[3]:
            if diagonals:
                for i, j in zip(range(line[0], line[2], np.sign(line[2] - line[0], dtype=int)),
                                range(line[1], line[3], np.sign(line[3] - line[1], dtype=int))):
                    ocean[i, j] += 1
                ocean[line[2], line[3]] += 1
            else:
                continue
        elif line[0] == line[2]:
            ocean[line[0], min(line[1], line[3]):max(line[1], line[3]) + 1] += 1
        else:
            ocean[min(line[0], line[2]): max(line[0],line[2]) + 1, line[1]] += 1

    print(np.sum(ocean >= 2))






if __name__ == "__main__":
    data = get_data()
    solution(data, diagonals=False)
    solution(data, diagonals=True)
