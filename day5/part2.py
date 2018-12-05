def prev_solution(input):
    input = list(input)
    trigger = True
    while trigger:
        for i, (a, b) in enumerate(zip(input, input[1:])):
            u, l = sorted([a, b])
            if u.isupper() and l.islower() and u.lower() == l:
                input.pop(i)
                input.pop(i)
                break
        else:
            trigger = False
    return len(input)


def solution(input):
    chars = set(input.lower())
    lowest = None
    for c in chars:
        new_input = input.replace(c, '')
        new_input = new_input.replace(c.upper(), '')
        l = prev_solution(new_input)
        if lowest is None or l < lowest:
            lowest = l
    return lowest


if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution(fh.read().strip()))
