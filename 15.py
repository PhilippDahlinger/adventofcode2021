from heapdict import heapdict

import numpy as np

def get_data(file):
    list_data = []
    for line in open(file, "r"):
        list_data.append([int(char) for char in line.strip()])
    data = np.array(list_data)
    return data


class Graph:
    def __init__(self, data):
        self.vertices = []
        self.data = data
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                self.vertices.append((i, j))
        self.target = (data.shape[0] -1, data.shape[1] -1)

    def get_dist(self, v1, v2):
        return self.data[v2]

    def get_neighbors(self, v):
        nbs = []
        if v[0] != 0:
            nbs.append((v[0] - 1, v[1]))
        if v[1] != 0:
            nbs.append((v[0], v[1] -1))
        if v[0] != self.data.shape[0] - 1:
            nbs.append((v[0] + 1, v[1]))
        if v[1] != self.data.shape[1] - 1:
            nbs.append((v[0], v[1] + 1))
        return nbs


def dijkstra(graph, source):
    Q = heapdict()
    prev = {}
    for v in graph.vertices:
        prev[v] = None
        Q[v] = np.Inf
    Q[source] = 0

    while len(Q) > 0:
        u, dist = Q.popitem()
        for nb in graph.get_neighbors(u):
            if nb in Q:
                alt = dist + graph.get_dist(u, nb)
                if alt < Q[nb]:
                    Q[nb] = alt
                    prev[nb] = u
    total_risk = 0
    v = graph.target
    while True:
        total_risk += graph.data[v]
        v = prev[v]
        if v == (0, 0):
            break

    return total_risk, prev


def first_solution(data):
    graph = Graph(data)
    source = (0, 0)
    print(dijkstra(graph, source)[0])

def second_solution(data):
    row = [data.copy()]
    for i in range(4):
        data = data + 1
        data[data == 10] = 1
        row.append(data.copy())
    row = np.concatenate(row, axis=1)
    tiled = [row.copy()]
    for j in range(4):
        row = row + 1
        row[row == 10] = 1
        tiled.append(row.copy())
    tiled = np.concatenate(tiled, axis=0)
    first_solution(tiled)




if __name__ == "__main__":
    data = get_data("data/15.txt")
    second_solution(data)

