import numpy as np
import collections
from tqdm import tqdm

def get_data(file):
    f = open(file, "r")
    init = f.readline().strip()
    f.readline()
    rules = {}
    for line in f:
        key, value = line.split("->")
        rules[key.strip()] = value.strip()
    return init, rules


def get_pairs(data):
    pairs = []
    for i in range(len(data) - 1):
        pairs.append(data[i:i + 2])
    return pairs

def build(data, rules):
    new_data = [data[0]]
    for i in range(len(data) - 1):
        # try:
        inserted = rules[data[i:i+2]]
        new_data += [inserted, data[i+1]]
        # except KeyError:
        #     new_data.append(p[i + 1])
    return new_data

def first_solution(data, rules, num_times):
    for _ in tqdm(range(num_times)):
        new_data = build(data, rules)
        data = "".join(new_data)

    c = collections.Counter(data)
    most_common_number = c.most_common(1)[0][1]
    least_common = min(c, key=c.get)
    print(most_common_number - data.count(least_common))


def second_solution(data, rules):
    qs = collections.defaultdict(lambda: 0)
    for i in range(len(data) - 1):
        qs[data[i:i+2]] += 1


    for _ in range(40):
        new_qs = collections.defaultdict(lambda: 0)
        for pair, count in qs.items():
            new_qs[f"{pair[0]}{rules[pair]}"] += count
            new_qs[f"{rules[pair]}{pair[1]}"] += count
        qs = new_qs
    letter_q = collections.defaultdict(lambda: 0)

    for key, value in qs.items():
        letter_q[key[0]] += value
    # gotta love python
    letter_q[key[1]] += 1
    vs = letter_q.values()
    print(max(vs) - min(vs))




if __name__ == "__main__":
    init, rules = get_data("data/14.txt")
    # first_solution(init, rules, num_times=10)
    second_solution(init, rules)