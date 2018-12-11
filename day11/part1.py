from itertools import product

def pl(x, y, s):
    return int(str((((x + 10) * y) + s) * (x + 10))[-3]) - 5

def solution1(input):
    grid = {}
    for x, y in product(range(1, 301), repeat=2):
        grid[(x, y)] = pl(x, y, input)
    
    max_p = 0
    max_xy = None
    for x, y in product(range(1, 301), repeat=2):
        try:
            p = sum(grid[(x + dx, y + dy)] for dx, dy in product(range(0, 3), repeat=2))
            if p > max_p:
                max_p = p
                max_xy = (x, y)
        except KeyError:
            continue
    return ','.join(map(str, max_xy))

def parse_input1(input):
    return int(input)


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))

