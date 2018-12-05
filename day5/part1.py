def solution(input):
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



if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution(fh.read().strip()))
