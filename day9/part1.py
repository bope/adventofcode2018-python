from collections import defaultdict

def solution1(players, stop):
    marbles = [0]
    current = 0

    steps = 0
    score = defaultdict(int)
    while steps <= stop:
        for player in range(1, players + 1):
            steps += 1

            if steps % 23 == 0:
                r = (current - 7) % len(marbles)
                score[player] += steps + marbles[r]
                del marbles[r]
                current = r
            else:
                insert = (current + 2) % len(marbles)
                if insert == 0:
                    insert = len(marbles)
                marbles.insert(insert, steps)
                current = insert

    return max(score.values())

def parse_input1(input):
    players, *_, stop, _ = input.split()
    return int(players), int(stop)

if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(*parse_input1(fh.read().strip())))