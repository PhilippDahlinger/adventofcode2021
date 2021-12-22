import numpy as np


def get_data():
    steps = []
    f = open("data/22.txt", "r")
    for line in f:
        state, coords = line.strip().split(" ")
        if state == "off":
            state = 0
        else:
            state = 1
        coords = coords.split(",")
        c_values = []
        for c in coords:
            relevant = c[2:]
            rel = relevant.split("..")
            c_values.append((int(rel[0]), int(rel[1])))
        steps.append((state, c_values))
    return steps


def first(steps):
    data = np.zeros((100, 100, 100))
    for step in steps:
        if np.abs(step[1][0][0]) > 100:
            continue
        state, coords = step
        data[coords[0][0] + 50:coords[0][1]+ 51, coords[1][0] + 50: coords[1][1] + 51, coords[2][0] + 50: coords[2][1] + 51] = state
        print(np.sum(data))

class Cube:
    def __init__(self):
        self.x = [0, 0]
        self.y = [0, 0]
        self.z = [0, 0]

    def __repr__(self):
        return f"x:{self.x}, y:{self.y}, z:{self.z}"

def second(steps):
    v = 0
    disjoints = []
    for step in steps:
        new_disjoints = []
        a = Cube()
        a.x = list(step[1][0])
        a.y = list(step[1][1])
        a.z = list(step[1][2])
        for b in disjoints:
            is_inter, c = intersection(a, b)
            if not is_inter:
                new_disjoints.append(b)
            else:
                subs = remove(b, c)
                new_disjoints += subs
        if step[0] == 1:
            new_disjoints.append(a)
        disjoints = new_disjoints
        v = 0
        for c in disjoints:
            v += (c.x[1] - c.x[0] + 1) * (c.y[1] - c.y[0] + 1) * (c.z[1] - c.z[0] + 1)
        print(v)

def intersection(a, b):
    # A is new cube, B old
    c = Cube()
    c.x[0] = max(a.x[0], b.x[0])
    c.x[1] = min(a.x[1], b.x[1])
    if c.x[1] < c.x[0]:
        return False, None
    c.y[0] = max(a.y[0], b.y[0])
    c.y[1] = min(a.y[1], b.y[1])
    if c.y[1] < c.y[0]:
        return False, None
    c.z[0] = max(a.z[0], b.z[0])
    c.z[1] = min(a.z[1], b.z[1])
    if c.z[1] < c.z[0]:
        return False, None
    return True, c

def remove(b, c):
    subs = []
    # removes c from b --> sub cubes
    if c.x[0] > b.x[0]:
        new = Cube()
        new.x = [b.x[0], c.x[0] - 1]
        new.y = b.y.copy()
        new.z = b.z.copy()
        subs.append(new)
    if c.x[1] < b.x[1]:
        new = Cube()
        new.x = [c.x[1] + 1, b.x[1]]
        new.y = b.y.copy()
        new.z = b.z.copy()
        subs.append(new)
    new_x = [max(c.x[0], b.x[0]), min(c.x[1], b.x[1])]
    if c.y[0] > b.y[0]:
        new = Cube()
        new.x = new_x.copy()
        new.y = [b.y[0], c.y[0] - 1]
        new.z = b.z.copy()
        subs.append(new)
    if c.y[1] < b.y[1]:
        new = Cube()
        new.x = new_x.copy()
        new.y = [c.y[1] + 1, b.y[1]]
        new.z = b.z.copy()
        subs.append(new)
    new_y = [max(c.y[0], b.y[0]), min(c.y[1], b.y[1])]
    if c.z[0] > b.z[0]:
        new = Cube()
        new.x = new_x.copy()
        new.y = new_y.copy()
        new.z = [b.z[0], c.z[0] - 1]
        subs.append(new)
    if c.z[1] < b.z[1]:
        new = Cube()
        new.x = new_x.copy()
        new.y = new_y.copy()
        new.z = [c.z[1] + 1, b.z[1]]
        subs.append(new)
    return subs


if __name__ == "__main__":
    steps = get_data()
    first(steps)
    second(steps)