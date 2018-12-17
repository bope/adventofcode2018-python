
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


def solution1(input):
    ret = 0
    for before, inst, after in input:
        opcodes = guess_opcode(before, inst, after)
        if len(opcodes) >= 3:
            ret += 1

    return ret
        


def parse_input1(input):
    samples, _ = input.split('\n\n\n')
    for sample in samples.split('\n\n'):
        before, inst, after = sample.strip().split('\n')
        before = [int(i.strip()) for i in before[9:-1].split(',')]
        inst = [int(i) for i in inst.split()]
        after = [int(i.strip()) for i in after[9:-1].split(',')]
        yield before, inst, after




if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read().strip())))
