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
    for i in range(1, padded.shape[0] -1):
        for j in range(1, padded.shape[1] -1):
            center = padded[i,j]
            if center < padded[i-1, j] and center < padded[i+1, j] and center < padded[i, j-1] and center < padded[i,j + 1]:
                risk += center + 1
    print(risk)

def second_solution(data):
    boarders = data == 9
    print("done")

if __name__ == "__main__":
    data = get_data("data/09.txt")
    second_solution(data)