from itertools import combinations


def solution(input):
    for a, b in combinations(input, 2):
        diff = 0
        same = []
        for ac, bc in zip(a, b):
            if ac != bc:
                diff += 1
                if diff > 1:
                    break
            else:
                same.append(ac)
        if diff == 1:
            return ''.join(same)


def parse_input(input):
    return input.split()


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution(parse_input(fh.read())))
