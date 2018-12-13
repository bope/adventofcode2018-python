import re


def format_state(state):
    change = 0
    while state[0] == '.':
        state.pop(0)
        change -= 1
    while state[-1] == '.':
        state.pop(-1)

    state = list('....') + state + list('....')
    change += 4
    return state, change


def calc_sum(state, extra):
    return sum(i - extra for i, p in enumerate(state) if p == '#')


def solution1(state, spread, generations):
    state, extra = format_state(state)

    for g in range(1, generations + 1):

        new = ['.'] * len(state)

        for p, r in spread:
            for i in range(2, len(state)-2):
                if state[i-2:i+3] == p:
                    new[i] = r

        new, change = format_state(new)
        extra += change
        if ''.join(state) == ''.join(new):
            extra += change * (generations - g)
            break
        state = new

    return calc_sum(state, extra)



def parse_input1(input):
    state, _, *spread = input.split('\n')
    _, state = state.split(':')
    state = list(state.strip())
    spread = [(list(p.strip()), r.strip()) for p, r in [s.split('=>') for s in spread]]
    return state, spread



if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(*parse_input1(fh.read().strip()), 50000000000))
