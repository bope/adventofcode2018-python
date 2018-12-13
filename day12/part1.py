import re

def solution1(state, spread, generations):
    extra = 0
    for g in range(0, generations):
        if '#' in state[:4]:
            state = list('....') + state
            extra += 4

        if '#' in state[-4:]:
            state = state + list('....')

        new = ['.'] * len(state)
    
        for p, r in spread:
            for i in range(2, len(state)-2):
                if state[i-2:i+3] == p:
                    new[i] = r
        state = new
    return sum(i - extra for i, p in enumerate(state) if p == '#')



def parse_input1(input):
    state, _, *spread = input.split('\n')
    _, state = state.split(':')
    state = list(state.strip())
    spread = [(list(p.strip()), r.strip()) for p, r in [s.split('=>') for s in spread]]
    return state, spread



if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(*parse_input1(fh.read().strip()), 20))
