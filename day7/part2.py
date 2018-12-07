
def solution1(input, worker_count):
    deps = {}

    for dep, char in input:
        if char not in deps:
            deps[char] = []

        for c in dep:
            deps[char].append(c)
            if c not in deps:
                deps[c] = []

    time = 0
    workers = []
    while True:
        wc = len(workers)
        fwc = worker_count - wc

        if fwc:
            steps = [c for c, d in sorted(deps.items(), key=lambda x: (len(x[1]), x[0])) if len(d) == 0]

            if not steps and len(workers) == 0:
                return time

            for step in steps[0:fwc]:
                workers.append([step, 60 + ord(step) - ord('A') + 1])
                deps.pop(step)

        free_worker = False
        while not free_worker:
            time += 1
            for i in range(len(workers)):
                workers[i][1] -= 1
                if workers[i][1] == 0:
                    for _, d in deps.items():
                        if workers[i][0] in d:
                            d.remove(workers[i][0])

                    free_worker = True
        workers = [w for w in workers if w[1] != 0]


def parse_input1(input):
    for i in input.split('\n'):
        _, f, *_, b, _, _ = i.split()
        yield f, b


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip()), 5))