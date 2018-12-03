def solution(freq, input):
    return freq + sum(input)

def parse_input(input):
    return map(int, input.split())

if __name__ == '__main__':
    with open('input.txt') as fh:
        print(solution(0, parse_input(fh.read())))
