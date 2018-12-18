from dataclasses import dataclass, astuple
from copy import deepcopy

@dataclass
class Pos:
    y: int
    x: int

    def __hash__(self):
        return hash(astuple(self))

    def __add__(self, other):
        return Pos(y=self.y + other.y, x=self.x + other.x)

    def __lt__(self, other):
        return astuple(self) < astuple(other)

    def neighbours(self, min_p, max_p):
        for x in range(-1, 2):
            for y in range(-1, 2):
                p = Pos(y=y, x=x) + self
                if p.x > max_p.x or p.y > max_p.y or p.x < min_p.x or p.y < min_p.y:
                    continue
                if p != self:
                    yield p

def print_map(forest):
    t = sorted(forest.items(), key=lambda x: x[0])
    l = None
    for p, c in t:
        if l is None or l.y != p.y:
            print('\n', end='')
        l = p
        print(c, end='')
    print('\n', end='')


def solution1(data, rounds):
    forest = {}
    min_p = None
    max_p = None
    for y, x, c in data:
        p = Pos(y=y, x=x)
        forest[p] = c
        if min_p is None:
            min_p = p
        if max_p is None:
            max_p = p

        min_p = min(min_p, p)
        max_p = max(max_p, p)

    for i in range(rounds):
        new_forest = deepcopy(forest)

        for pos, c in forest.items():
            adj = []
            for n in pos.neighbours(min_p, max_p):
                adj.append(forest[n])
            
            if c == '.' and adj.count('|') >= 3:
                new_forest[pos] = '|'
            elif c == '|' and adj.count('#') >= 3:
                new_forest[pos] = '#'
            elif c == '#':
                if adj.count('#') >= 1 and adj.count('|') >= 1:
                    new_forest[pos] = '#'
                else:
                    new_forest[pos] = '.'
    
        forest = new_forest
        print_map(forest)

    chars = list(forest.values())
    return chars.count('|') * chars.count('#')

def parse_input1(input):
    for y, line in enumerate(input.split('\n')):
        for x, c in enumerate(line):
            yield y, x, c


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read()), 10))
