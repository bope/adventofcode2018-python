from itertools import count

# left, straight, right

T_LEFT = -1
T_RIGHT = 1
T_STRAIGHT = 0

t_map = {
    T_LEFT: T_STRAIGHT,
    T_STRAIGHT: T_RIGHT,
    T_RIGHT: T_LEFT
}


D_UP = (-1, 0)
D_DOWN = (1, 0)
D_LEFT = (0, -1)
D_RIGHT = (0, 1)

t_list = [D_UP, D_RIGHT, D_DOWN, D_LEFT]

t_d_map = {
    '/': {
        D_UP: D_RIGHT,
        D_DOWN: D_LEFT,
        D_RIGHT: D_UP,
        D_LEFT: D_DOWN,
    },
    '\\': {
        D_UP: D_LEFT,
        D_DOWN: D_RIGHT,
        D_RIGHT: D_DOWN,
        D_LEFT: D_UP
    }
}

def turn(d, t):
    return t_list[(t_list.index(d) + t) % len(t_list)], t_map[t]


def drive(y, x, d):
    return y + d[0], x + d[1]


def solution1(input):
    carts = {}
    
    tracks = [list(l) for l in input.split('\n')]
    for y in range(len(tracks)):
        for x in range(len(tracks[y])):
            c = tracks[y][x]
            if c == '^':
                carts[(y, x)] = (D_UP, T_LEFT)
                tracks[y][x] = '|'
            elif c == 'v':
                carts[(y, x)] = (D_DOWN, T_LEFT)
                tracks[y][x] = '|'
            elif c == '>':
                carts[(y, x)] = (D_RIGHT, T_LEFT)
                tracks[y][x] = '-'
            elif c == '<':
                carts[(y, x)] = (D_LEFT, T_LEFT)
                tracks[y][x] = '-'


    for tick in count(1):
        oc = sorted(carts.items(), key=lambda x: x[0])
        for (y, x), (d, t) in oc:
            if (y, x) not in carts:
                continue
            carts.pop((y, x))
            c = tracks[y][x]
            if c == '+':
                d, t = turn(d, t)
            elif c in ['/', '\\']:
                d = t_d_map[c][d]

            ny, nx = drive(y, x, d)
            if (ny, nx) in carts:
                carts.pop((ny, nx))
                continue

            carts[(ny, nx)] = (d, t)

        cc = len(carts)
        if cc == 1:
            y, x = list(carts.keys())[0]
            return '{},{}'.format(x, y )


def parse_input1(input):
    return input


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution1(parse_input1(fh.read())))
    #with open('test.txt') as fh:
    #    print(solution1(parse_input1(fh.read())))
