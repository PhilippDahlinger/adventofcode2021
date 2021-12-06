import numpy as np
from tqdm import tqdm

def update(data):
    new_data = {-1: 0, 0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for i in data.keys():
        new_data[i-1] = data[i]
    babies = new_data.get(-1)

    del new_data[-1]
    new_data[8] += babies
    new_data[6] += babies
    return new_data

def print_data(data):
    for x in data.keys():
        print(f"{x}: {data[x]}")
    print("-----------------------------------------")

def get_data():
    data = np.loadtxt("data/06.txt", delimiter=",")
    return list(data)

if __name__ == "__main__":
    # data = [3,4,3,1,2]
    data = get_data()

    num_days = 80
    converted_data = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for x in data:
        converted_data[x] += 1
    for step in tqdm(range(num_days)):
        converted_data = update(converted_data)
    total = 0
    for key in converted_data:
        total += converted_data[key]
    print(total)