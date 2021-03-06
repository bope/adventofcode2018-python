from collections import defaultdict
import numpy as np

def solution1(input):
    m = defaultdict(lambda: defaultdict(int))
    for i, ol, ot, w, h in input:
        for x in range(ol, ol+w):
            for y in range(ot, ot+h):
                m[x][y] += 1

    for i, ol, ot, w, h in input:
        overlap = False
        for x in range(ol, ol+w):
            for y in range(ot, ot+h):
                if m[x][y] > 1:
                    overlap = True
                    break
            if overlap:
                break
        else:
            return i


def solution2(input):
    m = np.zeros((1000, 1000), dtype=int)
    for _, ol, ot, w, h in input:
        m[ol:ol+w,ot:ot+h] += 1

    for i, ol, ot, w, h in input:
        if np.count_nonzero(m[ol:ol+w,ot:ot+h] > 1) == 0:
            return i


def parse_input(input):
    for i in input.split('\n'):
        id, _, offset, size = i.split()
        o_l, o_t = offset[:-1].split(',')
        w, h = size.split('x')
        id = id[1:]
        yield id, int(o_l), int(o_t), int(w), int(h)


if __name__ == '__main__':
    # with open('input.txt') as fh:
    #     print(solution1(list(parse_input(fh.read().strip()))))
    with open('input.txt') as fh:
        print(solution2(list(parse_input(fh.read().strip()))))

