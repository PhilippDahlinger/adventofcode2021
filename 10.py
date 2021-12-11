import numpy as np


def get_data(file):
    data = []
    for line in open(file, "r"):
        data.append(line.strip())
    return data


class Node:
    def __init__(self, origin, opened):
        self.origin = origin
        self.opened = opened
        self.translator = {"(": ")", "[": "]", "{": "}", "<": ">", "a": "e"}

    def match(self, closed):
        return closed == self.translator[self.opened]


def first_solution(data):
    opened = ["(", "[", "{", "<"]
    score_translator = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for line in data:
        node = Node(None, "a")
        for char in line:
            if char in opened:
                node = Node(node, char)
            else:
                if node.match(char):
                    node = node.origin
                else:
                    print(line, f"Expected {node.translator[node.opened]}, but found {char}")
                    score += score_translator[char]
                    break
    print(score)

def second_solution(data):
    opened = ["(", "[", "{", "<"]
    score_translator = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    for line in data:
        use_line = True
        node = Node(None, "a")
        for char in line:
            if char in opened:
                node = Node(node, char)
            else:
                if node.match(char):
                    node = node.origin
                else:
                    use_line = False
                    break
        if use_line:
            close_string = ""
            while node.opened != "a":
                close_string += node.translator[node.opened]
                node = node.origin
            local_score = 0
            for char in close_string:
                local_score *= 5
                local_score += score_translator[char]
            scores.append(local_score)
    result = np.median(np.array(scores))
    print(int(result))



if __name__ == "__main__":
    data = get_data("data/10.txt")
    second_solution(data)