import numpy as np

def get_data(file):
    inp = []
    output = []
    for line in open(file, "r"):
        front, back = line.split("|")
        back_split = back.strip().split(" ")
        output.append(back_split)
        front_split = front.strip().split(" ")
        inp.append(front_split)
    return inp, output

def first_solution(output):
    output_len = np.array([[len(o) for o in row] for row in output]).reshape(-1)
    unique_lengths = [2, 3, 4, 7]
    result = 0
    for u in unique_lengths:
        result += np.sum(output_len == u)
    print(result)


def decode(output_row, mapping):
    decoder = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7,
               "abcdefg": 8, "abcdfg": 9}
    out_int = 0
    for idx, elem in enumerate(reversed(output_row)):
        real_signal = decoder["".join(sorted([mapping[char] for char in elem]))]
        out_int += real_signal * (10 ** idx)
    return out_int


def diff_length_by_one(a, b):
    # first is shorter
    for c in a:
        b = b.replace(c, "")
    return b


def get_mapping(inp_row):
    # mapping goes from scrambled to ordered
    mapping = {}
    inp_len = [len(i) for i in inp_row]
    # signal for a
    one = inp_row[inp_len.index(2)]
    seven = inp_row[inp_len.index(3)]
    four = inp_row[inp_len.index(4)]
    signal_for_a = diff_length_by_one(one, seven)
    mapping[signal_for_a] = "a"
    inp_row = [i.replace(signal_for_a, "") for i in inp_row]
    inp_len = [len(i) for i in inp_row]
    # signal for f and c
    five_segments = [i for i in inp_row if len(i) == 5]
    signal_for_f = list(set(five_segments[0]) & set(five_segments[1]) & set(five_segments[2]) & set(one))[0]
    mapping[signal_for_f] = "f"
    signal_for_c = diff_length_by_one(signal_for_f, one)
    mapping[signal_for_c] = "c"
    inp_row = [i.replace(signal_for_f, "") for i in inp_row]
    inp_row = [i.replace(signal_for_c, "") for i in inp_row]
    # signal for d
    two_segments = [i for i in inp_row if len(i) == 2]
    signal_for_d = list(set(two_segments[0]) & set(two_segments[1]))[0]
    mapping[signal_for_d] = "d"
    # signal for b
    signal_for_b = diff_length_by_one([signal_for_d, signal_for_c, signal_for_f], four)
    mapping[signal_for_b] = "b"
    # signal for g
    two_segments = [i.replace(signal_for_d, "") for i in two_segments]
    two_segments = [i.replace(signal_for_b, "") for i in two_segments]
    signal_for_g = [x for x in two_segments if len(x) == 1][0]
    mapping[signal_for_g] = "g"
    # last signal is missing --> can deduce
    signal_for_e = diff_length_by_one(list(mapping.keys()), "abcdefg")
    mapping[signal_for_e] = "e"

    return mapping



def second_solution(inp, output):
    result = 0
    for inp_row, output_row in zip(inp, output):
        map = get_mapping(inp_row)
        result += decode(output_row, map)
    print(result)



if __name__ == "__main__":
    inp, output = get_data("data/08.txt")
    # first_solution(output)
    second_solution(inp, output)