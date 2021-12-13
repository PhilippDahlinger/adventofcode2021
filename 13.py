import numpy as np


def get_data(file):
    lines = open(file, "r").readlines()
    points_str = lines[:lines.index("\n")]
    folds_str = lines[lines.index("\n") + 1:]
    points = set(tuple(int(coord) for coord in line.strip().split(",")) for line in points_str)
    folds = []
    for line in folds_str:
        equal = line.index("=")
        if line[equal - 1] == "x":
            direction = 0
        else:
            direction = 1
        folds.append((int(line.strip()[equal +1:]), direction))
    return points, folds


def folding(p, fold):
    axis = fold[1]
    if p[axis] < fold[0]:
        return p
    else:
        list_p = list(p)
        list_p[axis] = list_p[axis] - 2 * (list_p[axis] - fold[0])
        return tuple(list_p)


def first_solution(points, fold):
    new_points = set()
    for p in points:
        new_points.add(folding(p, fold))
    print(len(new_points))

def second_solution(points, folds):
    for fold in folds:
        new_points = set()
        for p in points:
            new_points.add(folding(p, fold))
        points = new_points
    result = np.zeros((300, 300))
    for p in points:
        result[p[1], p[0]] = 1
    print(result)
    # open it in the PyCharm debugger to see a spreadsheet of the np array with color grading. This allows us to see the letters easily.
    print("done")


if __name__ == "__main__":
    points, folds = get_data("data/13.txt")
    second_solution(points, folds)
