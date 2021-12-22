from collections import defaultdict


class Game:
    def __init__(self, pos1, pos2):
        self.p = [Player(pos1), Player(pos2)]
        self.dice = 1
        self.active = 0
        self.num_throws = 0

    def turn(self):
        rolled = 3 * self.dice + 3
        self.num_throws += 3
        self.dice += 3
        if self.dice > 100:
            self.dice -= 100
        if self.p[self.active].turn(rolled):
            # game over
            print(self.p[1 - self.active].score * self.num_throws)
            return False
        self.active = 1 - self.active
        return True

class Player:
    def __init__(self, pos):
        self.pos = pos
        self.score = 0
        self.max_score = 1000

    def turn(self, rolled):
        self.pos =  (self.pos + rolled) % 10
        if self.pos == 0:
            self.pos = 10
        self.score += self.pos
        if self.score >= self.max_score:
            return True


def first():
    g = Game(2, 7)
    while g.turn():
        pass

#########################################################################

def update(layer, turn, rolling_density, finished, goal_score=100):
    new_layer = defaultdict(lambda: 0)
    for state in layer.keys():
        is_finished = False
        for p in range(2):
            if state[p][1] >= goal_score:
                finished[p] += layer[state]
                is_finished = True
                break
        if is_finished:
            continue

        for roll in range(3, 10):
            old_p_state = state[turn]
            new_pos = old_p_state[0] + roll
            if new_pos > 10:
                new_pos -= 10
            new_score = old_p_state[1] + new_pos
            new_p_state = (new_pos, new_score)
            new_state = [None, None]
            new_state[turn] = new_p_state
            new_state[1 - turn] = state[1 - turn]
            new_state = tuple(new_state)
            new_layer[new_state] += rolling_density[roll] * layer[state]
    return new_layer




def second():
    rolling_density = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1,
    }
    finished = [0, 0]
    layer = {((2, 0), (7, 0)): 1}
    turn = 0
    while len(layer.keys()) > 0:
        print(len(layer.keys()))
        layer = update(layer, turn, rolling_density, finished)
        turn = 1 - turn


    print(finished)
    print([len(str(f)) for f in finished])

if __name__ == "__main__":
    # first()
    second()