from itertools import cycle

def solution(freq, input):
    freqs = {freq}
    for i in cycle(input):
        freq += i
        if freq in freqs:
            return freq
        freqs.add(freq)


def parse_input(input):
    return map(int, input.split())


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution(0, parse_input(fh.read())))
