
def solution1(input):
    deps = {}

    for dep, char in input:
        if char not in deps:
            deps[char] = []

        for c in dep:
            deps[char].append(c)
            if c not in deps:
                deps[c] = []

    order = []
    while True:
        steps = [c for c, d in sorted(deps.items(), key=lambda x: (len(x[1]), x[0])) if len(d) == 0]
        if not steps:
            return ''.join(order)

        step = steps[0]
        order.append(step)

        for _, d in deps.items():
            if step in d:
                d.remove(step)

        deps.pop(step)


def parse_input1(input):
    for i in input.split('\n'):
        _, f, *_, b, _, _ = i.split()
        yield f, b


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))