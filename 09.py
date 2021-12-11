import numpy as np

def get_data(file):
    list_data = []
    for line in open(file, "r"):
        list_data.append([int(char) for char in line.strip()])
    data = np.array(list_data)
    return data


def first_solution(data):
    padded = np.ones((data.shape[0] + 2, data.shape[1] + 2)) * 10
    padded[1:-1, 1: -1] = data
    risk = 0
    mins = []
    for i in range(1, padded.shape[0] -1):
        for j in range(1, padded.shape[1] -1):
            center = padded[i,j]
            if center < padded[i-1, j] and center < padded[i+1, j] and center < padded[i, j-1] and center < padded[i,j + 1]:
                mins.append((i,j))
                risk += center + 1
    print(risk)
    return mins

def second_solution(data, mins):
    padded = np.ones((data.shape[0] + 2, data.shape[1] + 2)) * 9
    padded[1:-1, 1: -1] = data
    boarders = np.array(padded == 9, dtype=int)
    sizes = []
    for (i, j) in mins:
        size = 0
        queue = [(i, j)]
        while len(queue) != 0:
            i, j = queue.pop()
            # expand
            if boarders[i,j] == 0:
                boarders[i, j] = 1
                size += 1
            for neighbor in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if boarders[neighbor[0], neighbor[1]] == 0:
                    queue.append(neighbor)
        sizes.append(size)
    sizes = sorted(sizes)
    print(sizes[-3] * sizes[-2] * sizes[-1])


if __name__ == "__main__":
    data = get_data("data/09.txt")
    mins = first_solution(data)
    second_solution(data, mins)