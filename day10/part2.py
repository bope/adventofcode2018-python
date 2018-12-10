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

    return min_dist_time

def parse_input1(input):
    for line in input.split('\n'):
        m = _re_line.match(line)
        yield int(m.group(1).strip()), int(m.group(2).strip()), int(m.group(3).strip()), int(m.group(4).strip())


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))
