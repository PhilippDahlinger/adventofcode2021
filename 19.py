import numpy as np

def get_data(file):
    scanners = []
    current_scanner = []
    for line in open(file, "r"):
        if line.startswith("---"):
            current_scanner = []
            continue
        if line != "\n":
            current_scanner.append(np.fromstring(line.strip(), sep=",", dtype=int))
        else:
            scanners.append(np.array(current_scanner))
    scanners.append(np.array(current_scanner))

    return scanners


def gen_dir_rots():
    dirs = [[1, 2, 3],
            [2, -1, 3],
            [-1, -2, 3],
            [-2, 1, 3],
            [3, 2, -1],
            [-3, 2, 1]]
    dir_rots = []
    for d in dirs:
        dir_rots += [d, [d[0], -d[2], d[1]], [d[0], -d[1], -d[2]], [d[0], d[2], -d[1]]]
    return dir_rots

class Scanner:
    dir_rots = gen_dir_rots()

    def __init__(self, data):
        self.data = data
        self.pairs_list = None
        self.pairs_set = None
        self.compute_pairs()
        self.pos = None


    def compute_pairs(self):
        self.pairs_list = []
        for i, b1 in enumerate(self.data):
            for j, b2 in enumerate(self.data):
                if i == j:
                    continue
                self.pairs_list.append(tuple(b1 - b2))
        self.pairs_set = set(self.pairs_list)
        self.pairs_list = np.array(self.pairs_list)

    def transform(self, dir_rot):
        dir = np.abs(dir_rot) - 1
        t = self.data[:, dir]
        t = t * np.sign(dir_rot, dtype=int)
        return t

    def transform_pairs(self, dir_rot):
        dir = np.abs(dir_rot, dtype=int) - 1
        t = self.pairs_list[:, dir]
        t = t * np.sign(dir_rot, dtype=int)
        p_list = []
        for entry in t:
            p_list.append(tuple(entry))
        return set(p_list)

    def _transform(self, dir_rot):
        self.data = self.transform(dir_rot)
        self.compute_pairs()

    def translate_to_global_system(self):
        assert self.pos is not None
        self.data = self.data + self.pos

    def __repr__(self):
        return repr(self.data)


def match(s1: Scanner, s2: Scanner):
    matched = False
    for d in Scanner.dir_rots:
        t_pairs = s2.transform_pairs(d)
        total_pairs = len(s1.pairs_set) + len(t_pairs)
        union = s1.pairs_set.union(t_pairs)
        sim = total_pairs - len(union)
        if sim >= 132:
            matched = True
            s2._transform(d)
            break
    if matched:
        # now in same coord system
        for ai in s1.data:
            diff_to_ai = set(map(tuple, s1.data - ai))
            for bj in s2.data:
                diff_to_bj = set(map(tuple, s2.data - bj))

                if len(diff_to_ai.intersection(diff_to_bj)) >= 12:
                    s2.pos = ai - bj
                    break
            if s2.pos is not None:
                break
        s2.translate_to_global_system()
        return True
    else:
        return False


def first_solution(scanners):
    unmatched = list(range(1, len(scanners)))
    matched = [0]
    while len(unmatched) > 0:
        for i in range(len(scanners)):
            if i not in matched:
                continue
            for j in range(len(scanners)):
                if j not in unmatched:
                    continue
                print(i,j)
                s1 = scanners[i]
                s2 = scanners[j]
                if match(s1, s2):
                    matched.append(j)
                    unmatched.remove(j)

    print("done")
    all_beacons = set()
    for s in scanners:
        all_beacons = all_beacons.union(set(map(tuple, s.data)))

    print(len(all_beacons))
    max_dist = 0
    scanners[0].pos = np.array([0,0,0])
    for s1 in scanners:
        for s2 in scanners:
            dist = np.sum(np.abs(s1.pos - s2.pos))
            max_dist = max(dist, max_dist)
    print(max_dist)



if __name__ == "__main__":
    d = get_data("data/19.txt")
    scanners = []
    for s_data in d:
        scanners.append(Scanner(s_data))
    first_solution(scanners)

