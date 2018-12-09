from collections import defaultdict

def solution1(players, stop):
    marbles = [0]
    current = 0
    stop *= 100
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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def pop(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.next = None
        self.prev = None

    def add(self, node):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node
        return node


def solution2(players, stop):
    current = Node(0)
    current.next = current
    current.prev = current
    stop *= 100
    steps = 0
    score = defaultdict(int)
    while steps <= stop:
        for player in range(1, players + 1):
            steps += 1
            if steps % 23 == 0:
                n = current.prev.prev.prev.prev.prev.prev.prev
                score[player] += steps + n.data
                current = n.next
                n.pop()
            else:
                current = current.next.add(Node(steps))
    return max(score.values())


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution2(*parse_input1(fh.read().strip())))
