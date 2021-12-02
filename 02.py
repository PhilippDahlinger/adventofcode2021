import numpy as np


def get_data():
    file = "data/02.txt"
    forward = []
    down = []
    up = []
    with open(file, "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith("forward"):
                forward.append(int(line[8:]))
                down.append(0)
                up.append(0)
            elif line.startswith("down"):
                down.append(int(line[5:]))
                forward.append(0)
                up.append(0)
            else:
                up.append(int(line[3:]))
                down.append(0)
                forward.append(0)
    return forward, down, up

def first_solution():
    forward, down, up = get_data()
    f_pos = np.sum(forward)
    d_pos = np.sum(down) - np.sum(up)
    print(f_pos, d_pos, f_pos*d_pos)



if __name__ == "__main__":
    f_data, d_data, u_data = get_data()
    f_pos = 0
    d_pos = 0
    aim = 0
    for f, d, u in zip(f_data, d_data, u_data):
        if f != 0:
            f_pos += f
            d_pos += aim * f
        elif d != 0:
            aim += d
        else:
            aim -= u
    print(f_pos, d_pos, f_pos * d_pos)