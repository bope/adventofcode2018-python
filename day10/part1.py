import re
from itertools import count
from collections import defaultdict

_re_line = re.compile(r'position=<(.+),(.+)> velocity=<(.+),(.+)>')

def solution1(input):
    input = list(input)
    min_dist = None
    min_dist_time = None
    for time in count():
        ys = [py + (vy * time) for _, py, _, vy in input]
        dist = max(ys) - min(ys)
        
        if min_dist is not None and dist > min_dist:
            break
        
        min_dist_time = time
        min_dist = dist

    pos = sorted([(px + (vx * min_dist_time), py + (vy * min_dist_time)) for px, py, vx, vy in input])
    xs, ys = zip(*pos)
    min_x, *_, max_x = sorted(xs)
    min_y, *_, max_y = sorted(ys)

    ret = ''
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in pos:
                ret += '#'
            else:
                ret += ' '
        ret += '\n'

    return ret

def parse_input1(input):
    for line in input.split('\n'):
        m = _re_line.match(line)
        yield int(m.group(1).strip()), int(m.group(2).strip()), int(m.group(3).strip()), int(m.group(4).strip())


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))
