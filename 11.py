import numpy as np

def get_data(file):
    list_data = []
    for line in open(file, "r"):
        list_data.append([int(char) for char in line.strip()])
    data = np.array(list_data)
    return data


def update(data):
    shape = data.shape
    flashed = np.zeros_like(data, dtype=bool)
    data += 1
    threshold = data > 9
    ind = np.nonzero(threshold)
    ind = (list(ind[0]), list(ind[1]))
    num_flahes = 0
    for i,j in zip(ind[0], ind[1]):
        if not flashed[i, j]:
            # flash
            flashed[i, j] = True
            num_flahes += 1
            x_nbs = [-1, 0, 1]
            y_nbs = [-1, 0, 1]
            if i == 0:
                x_nbs.remove(-1)
            elif i == shape[0] - 1:
                x_nbs.remove(1)
            if j == 0:
                y_nbs.remove(-1)
            elif j == shape[1] - 1:
                y_nbs.remove(1)
            for i_nb in x_nbs:
                for j_nb in y_nbs:
                    if i_nb == 0 and j_nb == 0:
                        continue
                    data[i + i_nb, j + j_nb] += 1
                    if data[i + i_nb, j + j_nb] > 9:
                        ind[0].append(i + i_nb)
                        ind[1].append(j + j_nb)
    data[data > 9] = 0
    return num_flahes


def first_solution(data):
    total_flashes = 0
    for _ in range(100):
        total_flashes += update(data)
        print(data)

    print(total_flashes)

def second_solution(data):
    episode = 0
    while True:
        episode += 1
        total_flashes = update(data)
        if total_flashes == np.prod(np.array(np.shape(data))):
            print(episode)
            break

if __name__ == "__main__":
    data = get_data("data/11.txt")
    second_solution(data)
