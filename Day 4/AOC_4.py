from header import print_header


def main():
    print_header()

    input_lines = open('input').read().splitlines()

    input_lines.sort()

    solution(input_lines)


def solution(input_lines):
    records = dict()
    guard = None

    for line in input_lines:
        action = line.split('] ')[1]
        time = int(line.split(':')[1][:2])
        if action.startswith('Guard'):
            guard = int(action.split(' ')[1][1:])
            if guard not in records:
                records[guard] = [[0]*60, 0]
        elif action.startswith('falls'):
            records[guard][1] = time
        elif action.startswith('wakes'):
            for i in range(records[guard][1], time):
                records[guard][0][i] += 1

    # part 1
    guard1 = max(records, key=lambda k: sum(records[k][0]))
    minute1 = records[guard1][0].index(max(records[guard1][0]))

    print("Solution to first part is: {}".format(guard1*minute1))

    # part 2
    guard2 = max(records, key= lambda k: max(records[k][0]))
    minute2 = records[guard2][0].index(max(records[guard2][0]))

    print("Solution to second part is: {}".format(guard2*minute2))


if __name__ == '__main__':
    main()
