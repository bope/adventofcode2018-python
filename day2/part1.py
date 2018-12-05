from collections import defaultdict


def solution1(input):
    two = 0
    three = 0
    for box in input:
        chars = set(box)
        two_f = False
        three_f = False
        for c in chars:
            count = box.count(c)
            if count == 2 and not two_f:
                two += 1
                two_f = True
            elif count == 3 and not three_f:
                three += 1
                three_f = True
    return two * three


def solution2(input):
    counts = defaultdict(set)
    for box in input:
        for c in set(box):
            counts[box.count(c)].add(box)
    return len(counts[2]) * len(counts[3])


def parse_input(input):
    return input.split()


if __name__ == '__main__':
    # with open('input.txt') as fh:
    #     print(solution1(parse_input(fh.read())))
    
    with open('input.txt') as fh:
        print(solution2(parse_input(fh.read())))
