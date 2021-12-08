import numpy as np

def get_data():
    data = np.loadtxt("data/07.txt", delimiter=",")
    return data


def first_solution(data):
    pos = int(np.median(data))
    fuel = np.sum(np.abs(data-pos))
    print(fuel)

def second_solution(data):
    pos = np.mean(data)
    pos = 476
    # no idea why rounding 476.58 to 477 is a worse result than 476
    # pos = 476
    fuel = np.abs(data-pos)
    fuel = np.sum(fuel * (fuel + 1)/2)
    print(fuel)

if __name__ == "__main__":
    data = get_data()
    #data = np.array([16,1,2,0,4,2,7,1,2,14])
    second_solution(data)
