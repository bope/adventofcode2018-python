from collections import defaultdict


def solution(input):
    m = defaultdict(lambda: defaultdict(int))
    for i, ol, ot, w, h in input:
        for x in range(ol, ol+w):
            for y in range(ot, ot+h):
                m[x][y] += 1

    c = 0
    for x in m:
        for y in m:
            if m[x][y] > 1:
                c += 1
    return c


def parse_input(input):
    for i in input.split('\n'):
        id, _, offset, size = i.split()
        o_l, o_t = offset[:-1].split(',')
        w, h = size.split('x')
        id = id[1:]
        yield id, int(o_l), int(o_t), int(w), int(h)


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution(list(parse_input(fh.read().strip()))))

