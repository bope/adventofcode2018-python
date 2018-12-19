
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



def solution1(ip, program):
    reg = [0, 0, 0, 0, 0, 0]
    while True:
        try:
            inst = program[reg[ip]]
        except IndexError:
            return reg[0]
        c, v = _ops[inst[0]](reg, *inst[1:])
        reg[c] = v
        reg[ip] += 1


def parse_input1(data):
    data = iter(data.split('\n'))
    ip = int(next(data)[3:])
    program = []
    for line in data:
        program.append([int(a) if a.isnumeric() else a for a in line.split()])
    return ip, program


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(*parse_input1(fh.read().strip())))
