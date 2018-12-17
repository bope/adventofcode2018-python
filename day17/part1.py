from itertools import product
from dataclasses import dataclass

@dataclass
class Position:
    y: int
    x: int

    def __add__(self, other):
        return Position(y=self.y + other.y, x=self.x + other.x)

    def __hash__(self):
        return hash((self.y, self.x))

DOWN = Position(y=1, x=0)
UP = Position(y=-1, x=0)
LEFT = Position(y=0, x=-1)
RIGHT = Position(y=0, x=1)


def print_map(data, still, dried):
    ys, xs = zip(*[(p.y, p.x) for p in data])
    min_x, *_, max_x = sorted(xs)
    min_y, *_, max_y = sorted(ys)
    for y in range(0, max_y + 1):
        for x in range(min_x, max_x + 1):
            p = Position(y=y, x=x)
            if p == Position(y=0, x=500):
                print('+', end='')
            elif p in data:
                print('#', end='')
            elif p in still :
                print('~', end='')
            elif p in dried:
                print('|', end='')
            else:
                print('.', end='')
        print('\n', end='')
    print(min_y)


def solution1(data):
    scans = set()

    for scan in data:
        for y, x in product(*scan):
            scans.add(Position(y=y, x=x))

    ys, xs = zip(*[(p.y, p.x) for p in scans])
    min_y, *_, max_y = sorted(ys)

    falling = {Position(y=0, x=500)}
    spreading = set()
    still = set()
    dried = set()

    while falling or spreading:
        if falling:
            pos = falling.pop()
            while True:
                npos = pos + DOWN

                if npos.y > max_y:
                    break

                if npos in scans:
                    spreading.add(pos)
                    break

                if npos.y >= min_y:
                    dried.add(npos)
                pos = npos

        elif spreading:
            pos = spreading.pop()
            tmp = set()
            rpos = pos
            lpos = pos
            is_still = True

            while True:
                rpos = rpos + RIGHT
                if rpos in scans:
                    break
                tmp.add(rpos)
                down = rpos + DOWN
                if down not in scans and down not in still:
                    falling.add(rpos)
                    is_still = False
                    break

            while True:
                lpos = lpos + LEFT
                if lpos in scans:
                    break
                tmp.add(lpos)
                down = lpos + DOWN
                if down not in scans and down not in still:
                    falling.add(lpos)
                    is_still = False
                    break

            if is_still:
                tmp.add(pos)
                still |= tmp
                dried -= tmp
                spreading.add(pos + UP)
            else:
                tmp.add(pos)
                dried |= tmp
                still -= tmp

    return len(still) + len(dried)

def parse_input1(input):
    scans = []
    for line in input.split('\n'):
        scan = {}
        values = line.split(',')
        for value in values:
            name, measure = value.split('=')
            name = name.strip()
            measure = measure.strip()
            if '..' in measure:
                f, t = measure.split('..')
                measure = list(range(int(f), int(t) + 1))
            else:
                measure = [int(measure)]

            scan[name] = measure

        scans.append((scan['y'], scan['x']))

    return scans
        


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))
