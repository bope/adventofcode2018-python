from datetime import datetime
from collections import defaultdict

def solution1(input):
    input = sorted(input, key=lambda x: x[0])
    guard = None
    guard_states = defaultdict(lambda: defaultdict(int))
    for i, (dt, msg) in enumerate(input):
        if '#' in msg:
            guard = int(msg.split()[1][1:])
        elif 'falls asleep' in msg:
            try:
                n = input[i+1][0].minute
            except IndexError:
                n = 60
            for i in range(dt.minute, n):
                guard_states[guard][i] += 1

    guard_id, hours = sorted(guard_states.items(), key=lambda x: sum(x[1].values()))[-1]
    return guard_id * sorted(hours.items(), key=lambda x: x[1])[-1][0]


def parse_input(input):
    for line in input.split('\n'):
        ts, msg = line.split(']')
        dt = datetime.strptime(ts[1:], '%Y-%m-%d %H:%M')
        yield dt, msg


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input(fh.read().strip())))
