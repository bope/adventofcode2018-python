from itertools import islice

def solution1(input):
    ret = 0
    cc = next(input)
    mc = next(input)

    if cc is None or mc is None:
        return ret

    ret += sum(solution1(input) for _ in range(cc))
    ret += sum(islice(input, mc))
    return ret


def parse_input1(input):
    return map(int, input.split())


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))