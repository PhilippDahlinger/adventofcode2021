import numpy as np


def to_binary(hex_packet):
    translator = {
        "0": [0, 0, 0, 0],
        "1": [0, 0, 0, 1],
        "2": [0, 0, 1, 0],
        "3": [0, 0, 1, 1],
        "4": [0, 1, 0, 0],
        "5": [0, 1, 0, 1],
        "6": [0, 1, 1, 0],
        "7": [0, 1, 1, 1],
        "8": [1, 0, 0, 0],
        "9": [1, 0, 0, 1],
        "A": [1, 0, 1, 0],
        "B": [1, 0, 1, 1],
        "C": [1, 1, 0, 0],
        "D": [1, 1, 0, 1],
        "E": [1, 1, 1, 0],
        "F": [1, 1, 1, 1],
    }
    result = []
    for c in hex_packet:
        result += translator[c]
    return result

def to_number(binary):
    out = 0
    for i, value in enumerate(reversed(binary)):
        out += value * 2**i
    return out


def decode_literal(data, start):
    start = start + 6

    binary_number = []
    while True:
        block = data[start: start + 5]
        binary_number += block[1:]
        start += 5
        if block[0] == 0:
            break
    literal = to_number(binary_number)
    end = start
    return literal, end


def decode_operator(data, start):
    subs = []
    I = data[start + 6]
    if I == 0:
        l = to_number(data[start + 7: start + 22])
        start = start + 22
        end = start + l
        while True:
            subs.append(Packet(data, start))
            start = subs[-1].end
            if start == end:
                break
        return subs, start
    else:
        l = to_number(data[start + 7: start + 18])
        start = start + 18
        for i in range(l):
            subs.append(Packet(data, start))
            start = subs[-1].end
        return subs, start




class Packet:
    def __init__(self, data, start):
        self.version = to_number(data[start:start+3])
        self.type = to_number(data[start+3:start+6])
        if self.type == 4:
            # literal
            self.literal, self.end = decode_literal(data, start)
        else:
            self.subs, self.end = decode_operator(data, start)

    def evaluate(self):
        if self.type == 4:
            return self.literal
        else:
            child_values = [p.evaluate() for p in self.subs]
            if self.type == 0:
                return sum(child_values)
            elif self.type == 1:
                return int(np.prod(child_values))
            elif self.type == 2:
                return min(child_values)
            elif self.type == 3:
                return max(child_values)
            elif self.type == 5:
                if child_values[0] > child_values[1]:
                    return 1
                else:
                    return 0
            elif self.type == 6:
                if child_values[0] < child_values[1]:
                    return 1
                else:
                    return 0
            elif self.type == 7:
                if child_values[0] == child_values[1]:
                    return 1
                else:
                    return 0



def first_solution(packet):
    version_sum = 0
    l = [packet]
    while len(l) > 0:
        p = l.pop()
        version_sum += p.version
        if p.type != 4:
            l += p.subs
    print(version_sum)




def get_data():

    for l in open("data/16.txt", "r"):
        data = l.strip()
        break
    return data

if __name__ == "__main__":
    data = to_binary(get_data())
    p = Packet(data, 0)
    # first_solution(p)
    print(p.evaluate())
    print("done")
