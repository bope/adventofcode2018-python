from collections import defaultdict
from itertools import product

def solution1(input):
    input = list(input)
    xs = list(zip(*input))[0]
    ys = list(zip(*input))[1]
    max_x = max(xs)
    min_x = min(xs)
    max_y = max(ys)
    min_y = min(ys)
    sizes = defaultdict(int)

    dist_map = defaultdict(lambda: defaultdict(lambda: None))

    for i, (x, y) in enumerate(input):
        for mx, my in product(range(min_x, max_x + 1), range(min_y, max_y + 1)):
            dist = abs(mx - x) + abs(my - y)

            cell = dist_map[mx][my]

            if cell is None:
                dist_map[mx][my] = (i, dist)
                continue

            if cell[1] > dist:
                if cell[0] is not None:
                    sizes[cell[0]] -= 1
                sizes[i] += 1
                dist_map[mx][my] = (i, dist)
            elif cell[1] == dist:
                if cell[0] is not None:
                    sizes[cell[0]] -= 1
                dist_map[mx][my] = (None, dist)

    return max(sizes.values())




def parse_input1(input):
    for i in input.split('\n'):
        yield [int(x.strip()) for x in i.split(',')]


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))