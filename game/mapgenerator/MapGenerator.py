
import random


class MapGenerator:
    def __init__(self):
        self.size: int = 15
        self.enable_box_generation = False
        self.level = [[0 for x in range(self.size)] for x in range(self.size)]

        self.generate_walls()

    # TODO: do not spawn boxes near user and enemy. should be able to put bomb and not die
    def generate_boxes(self, p_i, p_j):
        # get cells round the pillar
        lists_round_boxes = [{
            "i": p_i - 1,
            "j": p_j - 1
        }, {
            "i": p_i + 1,
            "j": p_j + 1
        }, {
            "i": p_i + 1,
            "j": p_j - 1
        }, {
            "i": p_i - 1,
            "j": p_j + 1
        }, {
            "i": p_i,
            "j": p_j - 1
        }, {
            "i": p_i,
            "j": p_j + 1
        }, {
            "i": p_i - 1,
            "j": p_j
        }, {
            "i": p_i + 1,
            "j": p_j
        }]

        random_list = random.sample(range(0, 10), 8)

        magic_random_number = 3
        for i in range(len(lists_round_boxes)):
            if random_list[i] > magic_random_number:
                self.level[lists_round_boxes[i]['i']][lists_round_boxes[i]['j']] = 2

    def generate_walls(self):
        for i in range(self.size):
            self.level[0][i] = 1  # up line
            self.level[i][0] = 1  # left line
            self.level[i][self.size - 1] = 1  # right line
            self.level[self.size - 1][i] = 1  # down line
            for j in range(self.size):
                if 0 < i < self.size - 1:
                    if 0 < j < self.size - 1:
                        if i % 2 == 0 and j % 2 == 0:
                            self.level[i][j] = 1
                            if self.enable_box_generation:
                                self.generate_boxes(i, j)

    def get_map(self):
        return self.level

