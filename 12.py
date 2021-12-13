from collections import defaultdict
from copy import deepcopy
graph = {}

def get_raw_data(file):
    lines = [line.strip() for line in open(file, "r")]
    return lines

def create_graph(data):
    graph = defaultdict(lambda: set())
    for line in data:
        first, second = line.split("-")
        graph[first].add(second)
        graph[second].add(first)
    return graph


class Path:
    def __init__(self, visited, new_pos):
        self.visited = deepcopy(visited)
        self.visited.append(new_pos)

    def explore(self, graph, finished_paths):
        if self.visited[-1] == "end":
            finished_paths.append(self)
            return []
        new_paths = []
        for nb in graph[self.visited[-1]]:
            if nb.isupper() or nb not in self.visited:
                new_paths.append(Path(self.visited, nb))
        return new_paths

    def __str__(self):
        result = ""
        for nb in self.visited:
            result += f"{nb}-"
        result = result[:-1]
        return result


class Path2(Path):
    def __init__(self, visited, new_pos, used_small_cave):
        super().__init__(visited, new_pos)
        self.used_small_cave = used_small_cave

    def explore(self, graph, finished_paths):
        if self.visited[-1] == "end":
            finished_paths.append(self)
            return []
        new_paths = []
        for nb in graph[self.visited[-1]]:
            if nb == "start":
                continue
            if nb.isupper():
                new_paths.append(Path2(self.visited, nb, self.used_small_cave))
            else:
                if nb not in self.visited:
                    new_paths.append(Path2(self.visited, nb, self.used_small_cave))
                else:
                    if not self.used_small_cave:
                        new_paths.append(Path2(self.visited, nb, True))
        return new_paths


def first_solution(graph):
    finished_paths = []
    paths = [Path([], "start")]
    while len(paths) != 0:
        new_paths = []
        for path in paths:
            new_paths = new_paths + path.explore(graph, finished_paths)
        paths = new_paths
    for path in finished_paths:
        print(path)
    print(len(finished_paths))

def second_solution(graph):
    finished_paths = []
    paths = [Path2([], "start", False)]
    while len(paths) != 0:
        new_paths = []
        for path in paths:
            new_paths = new_paths + path.explore(graph, finished_paths)
        paths = new_paths
    for path in finished_paths:
        print(path)
    print(len(finished_paths))





if __name__ == "__main__":
    data = get_raw_data("data/12.txt")
    graph = create_graph(data)
    # first_solution(graph)
    second_solution(graph)