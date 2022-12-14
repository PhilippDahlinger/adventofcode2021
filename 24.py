class ALU:
    def __init__(self):
        self.z = 0
        self.a_list = [12, 14, 11, -9, -7]
        self.b_list = [15, 12, 15, 12, 15]
        self.c_list = [1, 1, 1, 26, 26]

    def cycle(self, w, a, b, c):
        x = self.z % 26 + a
        if x == w:
            x = 0
        else:
            x = 1
        y1 = 25 * x + 1
        y2 = (w + b) * x
        self.z = (self.z // c) * y1 + y2

    def test_w(self, w_list):
        self.z = 0
        for w,a,b,c in zip(w_list, self.a_list, self.b_list, self.c_list):
            self.cycle(w, a, b, c)
        if 17 <= self.z <= 25:
            print(self.z, w_list)

    def brute_force(self):
        for w1 in range(1,10):
            for w2 in range(1, 10):
                for w3 in range(1, 10):
                    for w4 in range(1, 10):
                        for w5 in range(1, 10):
                            w_list = [w1, w2, w3, w4, w5]
                            self.test_w(w_list)

if __name__ == "__main__":
    w_list = [1,1,1,1,1]
    alu = ALU()
    alu.brute_force()
    # first 5 numbers:
    # 9, 4, 3, 9, 9
    z = 24

    # second puzzle:
    # first 5 numbers:
    # 2, 1, 1, 7, 6
    z = 17

