def solution1(input):
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


def solution2(input):
    input = list(input)
    i = 0
    while True:
        try:
            a = input[i]
            b = input[i+1]
        except IndexError:
            return len(input)

        if a != b and a.lower() == b.lower():
            input.pop(i)
            input.pop(i)
            i -= 1
        else:
            i += 1


if __name__ == '__main__':
    #with open('input.txt') as fh:
    #    print(solution1(fh.read().strip()))

    with open('input.txt') as fh:
        print(solution2(fh.read().strip()))
    
