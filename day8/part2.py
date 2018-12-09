from itertools import islice

def solution1(input):
    ret = 0
    cc = next(input)
    mc = next(input)

    if cc is None or mc is None:
        return ret

    cn = {i: solution1(input) for i in range(cc)}
    m = list(islice(input, mc))

    if cc == 0:
        return sum(m)

    return sum(cn.get(i - 1, 0) for i in m if i)


def parse_input1(input):
    return map(int, input.split())


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))
