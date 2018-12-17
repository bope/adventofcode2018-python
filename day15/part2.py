from dataclasses import dataclass


@dataclass
class Position:
    y: int
    x: int
    
    def __add__(self, other):
        return Position(y=self.y + other.y, x=self.x + other.x)

    def neighbours(self):
        return [self + o for o in _neighbours]

    def __hash__(self):
        return hash((self.y, self.x))

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

_neighbours = [
    Position(y=-1, x=0),  # up
    Position(y=0, x=-1),  # left
    Position(y=0, x=1),   # right
    Position(y=1, x=0),   # down
]


@dataclass
class Unit:
    position: Position
    team: str
    hp: int
    atk: int

    def do(self, cave, units):
        if self.hp <= 0:
            return

        units = [u for u in units if u.hp > 0 and u != self]
        targets = [u for u in units if u.team != self.team]
        targets_pos = [u.position for u in targets]
        units_pos = [u.position for u in units]

        to_visit = []
        visited = set()
        taken = set()
        distance = {}
        path = {}

        target_pos = None
        distance[self.position] = 0
        to_visit = [self.position]
        taken.add(self.position)
        
        while len(to_visit) > 0:
            pos = to_visit.pop(0)
            if pos in visited:
                continue
            visited.add(pos)

            if pos in cave:
                continue

            if pos in targets_pos:
                # found closest enemy
                target_pos = pos
                break

            if pos in units_pos:
                continue

            for npos in pos.neighbours():

                if npos in visited:
                    continue
                if npos in taken:
                    continue

                distance[npos] = distance[pos] + 1
                path[npos] = pos
                to_visit.append(npos)
                taken.add(npos)
        
        if not target_pos:
            return None

        res = ''
        target = targets[targets_pos.index(target_pos)]
        move_pos = target_pos
        if move_pos != self.position:
            while True:
                if distance[move_pos] == 1:
                    break
                move_pos = path[move_pos]
            if move_pos != target_pos: 
                res += '{} -> {}'.format(self.position, move_pos)
                self.position = move_pos
        
        close_targets = [t for pos in self.position.neighbours() for t in targets if t.position == pos]
        if close_targets:
            low_hp_target = min(close_targets, key=lambda x: x.hp)
            low_hp_target.hp -= self.atk
            res += ' attacked {}'.format(low_hp_target)
               
        return res

def sort_units(units):
    return sorted(units, key=lambda x: x.position)


def print_map(cave, units):
    alive_units = [u for u in units if u.hp > 0]
    alive_units_pos = [u.position for u in alive_units]
    
    max_p = max(cave)
    for y in range(0, max_p.y + 1):
        for x in range(0, max_p.y + 1):
            p = Position(y=y, x=x)
            if p in alive_units_pos:
                print(alive_units[alive_units_pos.index(p)].team, end='')
            elif p in cave:
                print('#', end='')
            else:
                print('.', end='')
        print('\n', end='')


from itertools import count
from copy import deepcopy
def solution1(cave, units):
    o_units = sort_units(units)
    done = False
    
    for eatk in count(4):
        units = deepcopy(o_units)

        for u in units:
            if u.team == 'E':
                u.atk = eatk

        for i in count(1):
            res = []
            units = sort_units(units)
            for unit in units:
                res.append(unit.do(cave, sort_units(units)))
            
            if any(u.team == 'E' and u.hp <= 0 for u in units):
                break

            if all(r is None for r in res):
                done = True
                break
            print_map(cave, units)

        if done:
            break

    return sum(u.hp for u in units if u.hp > 0) * (i-2)

def parse_input1(input):
    cave = set()
    units = []
    for y, l in enumerate(input.split('\n')):
        for x, c in enumerate(l):
            p = Position(y=y, x=x)
            if c in 'GE':
                u = Unit(position=p, team=c, hp=200, atk=3)
                units.append(u)
            elif c == '#':
                cave.add(p)
    return cave, units

if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(*parse_input1(fh.read())))
