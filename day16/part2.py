from collections import defaultdict
_ops = {
    'addr': lambda r, a, b, c: (c, r[a] + r[b]),
    'addi': lambda r, a, b, c: (c, r[a] + b),
    'mulr': lambda r, a, b, c: (c, r[a] * r[b]),
    'muli': lambda r, a, b, c: (c, r[a] * b),
    'banr': lambda r, a, b, c: (c, r[a] & r[b]),
    'bani': lambda r, a, b, c: (c, r[a] & b),
    'borr': lambda r, a, b, c: (c, r[a] | r[b]),
    'bori': lambda r, a, b, c: (c, r[a] | b),
    'setr': lambda r, a, b, c: (c, r[a]),
    'seti': lambda r, a, b, c: (c, a),
    'gtir': lambda r, a, b, c: (c, int(a > r[b])),
    'gtri': lambda r, a, b, c: (c, int(r[a] > b)),
    'gtrr': lambda r, a, b, c: (c, int(r[a] > r[b])),
    'eqir': lambda r, a, b, c: (c, int(a == r[b])),
    'eqri': lambda r, a, b, c: (c, int(r[a] == b)),
    'eqrr': lambda r, a, b, c: (c, int(r[a] == r[b])),
}


def guess_opcode(before, inst, after):
    match = set()
    for k, f in _ops.items():
        b = before.copy()
        
        c, v = f(b, *inst[1:])
        b[c] = v
        if b == after:
            match.add(k)
    return match


def solution1(samples, program):
    opcodes_g = defaultdict(set)
    for before, inst, after in samples:
        opcodes = guess_opcode(before, inst, after)
        i = inst[0]
        if i not in opcodes_g:
            opcodes_g[i] = opcodes
        else:
            opcodes_g[i] &= opcodes

    while any(len(gs) > 1 for gs in opcodes_g.values()):
        ss = [s for s in list(opcodes_g.values()) if len(s) == 1]
        for i, s in opcodes_g.items():
            if len(s) > 1:
                for o in ss:
                    s -= o

    opcodes = {i: list(s)[0] for i, s in opcodes_g.items()}
    r = [0, 0, 0, 0]
    for inst in program:
        c, v = _ops[opcodes[inst[0]]](r, *inst[1:])
        r[c] = v
    
    return r[0]
        


def parse_input1(input):
    samples, program = input.split('\n\n\n')
    s = []
    for sample in samples.split('\n\n'):
        before, inst, after = sample.strip().split('\n')
        before = [int(i.strip()) for i in before[9:-1].split(',')]
        inst = [int(i) for i in inst.split()]
        after = [int(i.strip()) for i in after[9:-1].split(',')]
        s.append((before, inst, after))

    p = []
    for l in program.split('\n'):
        l = l.strip()
        if not l:
            continue
        p.append([int(i) for i in l.split()])

    return s, p



if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(*parse_input1(fh.read().strip())))
