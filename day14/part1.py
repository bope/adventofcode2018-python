class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def add(self, node):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node
        return node


def solution1(count):
    head = Node(3)
    head.next = head
    head.prev = head
    tail = head.add(Node(7))

    elves = [head, tail]
    recipe_count = 2

    while True:
        rsum = sum(elf.data for elf in elves)
        for char in str(rsum):
            recipe_count += 1
            tail = tail.add(Node(int(char)))

        for i in range(len(elves)):
            steps = elves[i].data + 1
            for _ in range(steps):
                elves[i] = elves[i].next

        if recipe_count == (count + 10):
            break

    c = tail
    s = ''
    for _ in range(10):
        s = str(c.data) + s
        c = c.prev

    return s

def parse_input1(input):
    return int(input)

if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))
