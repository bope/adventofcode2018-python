from itertools import product

def pl(x, y, s):
    return int(str((((x + 10) * y) + s) * (x + 10))[-3]) - 5

def solution1(input):
    grid = {}
    for x, y in product(range(1, 301), repeat=2):
        grid[(x, y)] = pl(x, y, input)
    
    max_p = 0
    max_xys = None
    for x, y in product(range(1, 301), repeat=2):
        ps = None
        for s in range(1, 301):
            try:
                if ps is None:
                    ps = grid[(x, y)]
                else:
                    ps += sum(grid[(dx, y + s - 1)] for dx in range(x, x + s))
                    ps += sum(grid[(x + s - 1, dy)] for dy in range(y, y + s - 1))
            except KeyError:
                break
    
            if ps > max_p:
                max_p = ps
                max_xys = (x, y, s)
    return ','.join(map(str, max_xys))

def parse_input1(input):
    return int(input)


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))

