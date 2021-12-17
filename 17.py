def simulate(x_v, y_v, target):
    highest_pos = 0
    pos = [0, 0]
    while True:
        pos[0] += x_v
        pos[1] += y_v
        if pos[1] > highest_pos:
            highest_pos = pos[1]
        if x_v > 0:
            x_v -= 1
        elif x_v < 0:
            x_v += 1
        y_v -= 1

        if target[0] <= pos[0] <= target[1] and target[2] <= pos[1] <= target[3]:
            return True, highest_pos
        if target[2] > pos[1] and y_v < 0:
            return False, highest_pos













if __name__ == "__main__":
    target = [144, 178, -100, -76]
    # test_target = [20, 30, -10, -5]

    best_height = 0
    total_hits = 0
    for x in range(0, 200):
        for y in range(-100, 100):
            hit, height = simulate(x, y, target)
            if hit:
                best_height = max(best_height, height)
                total_hits += 1
    print(best_height)
    print(total_hits)