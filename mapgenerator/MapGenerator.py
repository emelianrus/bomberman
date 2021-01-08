import pprint
import random

level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def generate_boxes(i, j):
    lists = [{
        "i": i - 1,
        "j": j - 1
    }, {
        "i": i + 1,
        "j": j + 1
    }, {
        "i": i + 1,
        "j": j - 1
    }, {
        "i": i - 1,
        "j": j + 1
    }, {
        "i": i,
        "j": j - 1
    }, {
        "i": i,
        "j": j + 1
    }, {
        "i": i - 1,
        "j": j
    }, {
        "i": i + 1,
        "j": j
    }]

    random_list = random.sample(range(0, 10), 8)

    magic_random_number = 3
    for i in range(len(lists)):
        if random_list[i] > magic_random_number:
            level[lists[i]['i']][lists[i]['j']] = 4


for i in range(len(level)):
    level[0][i] = 1  # up
    level[i][0] = 1  # left
    level[i][len(level)-1] = 1  # right
    level[len(level)-1][i] = 1  # down
    for j in range(len(level)):
        if 0 < i < len(level)-1:
            if 0 < j < len(level) - 1:
                if i % 2 == 0 and j % 2 == 0:
                    level[i][j] = 1
                    generate_boxes(i,j)


pp = pprint.PrettyPrinter()
pp.pprint(level)
