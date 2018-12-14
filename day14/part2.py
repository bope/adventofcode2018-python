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
    count = str(count)[::-1]

    while True:
        rsum = sum(elf.data for elf in elves)
        last_recipe_count = recipe_count
        for char in str(rsum):
            recipe_count += 1
            tail = tail.add(Node(int(char)))
            c = tail
            for i in range(len(count)):
                if str(c.data) != count[i]:
                    break
            
                if c is head:
                    break

                c = c.prev
            else:
                return recipe_count - len(count)

        for i in range(len(elves)):
            steps = elves[i].data + 1
            for _ in range(steps):
                elves[i] = elves[i].next


def parse_input1(input):
    return int(input)


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))
