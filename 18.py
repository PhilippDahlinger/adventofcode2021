
def parse(s):

    if len(s) == 1:
        root = Leaf(None, None, None, int(s[0]))
        return Tree(root, root, root)

    bracket_counter = 0
    separator = 0
    for i, c in enumerate(s):
        if c == "[":
            bracket_counter += 1
        elif c == "]":
            bracket_counter -= 1
        elif c == "," and bracket_counter == 1:
            separator = i
            break
    left_tree = parse(s[1: separator])
    right_tree = parse(s[separator + 1: -1])
    return concat_trees(left_tree, right_tree)


def concat_trees(t1, t2):
    new_root = Node(None, t1.root, t2.root)
    t1.right_leaf.right_nb = t2.left_leaf
    t2.left_leaf.left_nb = t1.right_leaf
    t1.root.top = new_root
    t2.root.top = new_root
    for node in t1:
        node.level += 1
    for node in t2:
        node.level += 1
    return Tree(new_root, t1.left_leaf, t2.right_leaf)


def add(t1, t2):
    t = concat_trees(t1, t2)
    while True:
        exploded = t.explode()
        if not exploded:
            splitted = t.split()
            if not splitted:
                break
    return t

class Node:
    def __init__(self, top, left, right):
        self.top = top
        self.left = left
        self.right = right
        if self.top is None:
            self.level = 0
        else:
            self.level = self.top.level + 1


    def explode(self, tree):
        assert self.level == 4
        assert type(self.left) == Leaf and type(self.right) == Leaf
        left_leaf = self.left.left_nb
        right_leaf = self.right.right_nb
        if left_leaf is not None:
            left_leaf.value += self.left.value
        if right_leaf is not None:
            right_leaf.value += self.right.value
        top = self.top
        new_leaf = Leaf(top, left_leaf, right_leaf, 0)
        if left_leaf is not None:
            left_leaf.right_nb = new_leaf
        if right_leaf is not None:
            right_leaf.left_nb = new_leaf
        if top.left is self:
            top.left = new_leaf
        else:
            top.right = new_leaf

        if left_leaf is None:
            tree.left_leaf = new_leaf
        if right_leaf is None:
            tree.right_leaf = new_leaf

    def mag(self):
        return 3 * self.left.mag() + 2 * self.right.mag()

    def __repr__(self):
        return f"[{repr(self.left)},{repr(self.right)}]"


class Leaf:
    def __init__(self, top, left_nb, right_nb, value):
        self.top = top
        self.left_nb = left_nb
        self.right_nb = right_nb
        self.value = value

    def __repr__(self):
        return str(self.value)

    def split(self, tree):
        assert self.value >= 10
        top = self.top
        assert type(top) == Node
        new_node = Node(top, None, None)
        left_leaf = Leaf(new_node, self.left_nb, None, self.value // 2)
        right_leaf = Leaf(new_node, left_leaf, self.right_nb, self.value // 2 + self.value % 2)
        left_leaf.right_nb = right_leaf
        new_node.left = left_leaf
        new_node.right = right_leaf

        if self.left_nb is not None:
            self.left_nb.right_nb = left_leaf
        if self.right_nb is not None:
            self.right_nb.left_nb = right_leaf

        if top.left == self:
            top.left = new_node
        else:
            top.right = new_node
        if tree.left_leaf is self:
            tree.left_leaf = left_leaf
        if tree.right_leaf is self:
            tree.right_leaf = right_leaf

    def mag(self):
        return self.value




class Tree:
    def __init__(self, root, left_leaf: Leaf, right_leaf: Leaf):
        self.root = root
        self.left_leaf = left_leaf
        self.right_leaf = right_leaf

    def explode(self):
        for l in self.iter_leaves():
            node = l.top
            if node.level == 4:
                node.explode(self)
                return True
        return False

    def split(self):
        for l in self.iter_leaves():
            if l.value >= 10:
                l.split(self)
                return True
        return False

    def __repr__(self):
        return f"Tree({repr(self.root)})"

    def __iter__(self):
        new_nodes = [self.root] if type(self.root) == Node else []
        while len(new_nodes) != 0:
            n = new_nodes.pop()
            if type(n.left) == Node:
                new_nodes.append(n.left)
            if type(n.right) == Node:
                new_nodes.append(n.right)
            yield n

    def iter_leaves(self):
        leaf = self.left_leaf
        while leaf is not None:
            yield leaf
            leaf = leaf.right_nb

    def mag(self):
        return self.root.mag()



def get_data(file):
    rows = []
    for row in open(file, "r"):
        rows.append(row.strip())
    return rows


def first_solution():
    data = get_data("data/18.txt")
    t = parse(data[0])
    for row in data[1:]:
        t2 = parse(row)
        t = add(t, t2)
    print(t.mag())

def second_solution():
    data = get_data("data/18.txt")
    high_mag = 0
    for i, d1 in enumerate(data):
        for j, d2 in enumerate(data):
            if i == j:
                continue
            mag = add(parse(d1), parse(d2)).mag()
            high_mag = max(high_mag, mag)
    print(high_mag)



if __name__ == "__main__":
    second_solution()