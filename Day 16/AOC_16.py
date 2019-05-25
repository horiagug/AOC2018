from header import print_header


def main():
    print_header()

    OPERATIONS = [
        addr, addi,
        mulr, muli,
        banr, bani,
        borr, bori,
        setr, seti,
        gtir, gtri, gtrr,
        eqir, eqri, eqrr
    ]

    # Before, Op, After
    sol1, codes = solve1(OPERATIONS)
    print('Solution to part 1 is: {}'.format(sol1))

    print('Solution to part 2 is: {}'. format(solve2(codes)))


def addr(a, b, c, regs):
    regs[c] = regs[a] + regs[b]
    return regs


def addi(a, b, c, regs):
    regs[c] = regs[a] + b
    return regs


def mulr(a, b, c, regs):
    regs[c]= regs[a] * regs[b]
    return regs


def muli(a, b, c, regs):
    regs[c] = regs[a] * b
    return regs


def banr(a, b, c, regs):
    regs[c] = regs[a] & regs[b]
    return regs


def bani(a, b, c, regs):
    regs[c] = regs[a] & b
    return regs


def borr(a, b, c, regs):
    regs[c] = regs[a] | regs[b]
    return regs


def bori(a, b, c, regs):
    regs[c] = regs[a] | b
    return regs


def setr(a, b, c, regs):
    regs[c] = regs[a]
    return regs


def seti(a, b, c, regs):
    regs[c] = a
    return regs


def gtir(a, b, c, regs):
    regs[c] = int(a > regs[b])
    return regs


def gtri(a, b, c, regs):
    regs[c] = int(regs[a] > b)
    return regs


def gtrr(a, b, c, regs):
    regs[c] = int(regs[a] > regs[b])
    return regs


def eqir(a, b, c, regs):
    regs[c] = int(a == regs[b])
    return regs


def eqri(a, b, c, regs):
    regs[c] = int(regs[a] == b)
    return regs


def eqrr(a, b, c, regs):
    regs[c] = int(regs[a] == regs[b])
    return regs


def solve1(OPERATIONS):
    before = []
    op = []
    after = []

    # Read the first part instructions save data to lists
    with open('input1') as f:
        lines = (line.rstrip() for line in f)
        lines = (line for line in lines if line)
        for line in lines:
            line = line.strip('\n')
            if 'Before' in line:
                split = line.split(',')
                before.append((int(split[0][-1:]), int(split[1][-1:]), int(split[2][-1:]), int(split[3][-2:-1])))
            elif 'After' in line:
                split = line.split(',')
                after.append((int(split[0][-1:]), int(split[1][-1:]), int(split[2][-1:]), int(split[3][-2:-1])))

            elif 'After' not in line and 'Before' not in line:
                split = line.split(' ')
                op.append((int(split[0]), int(split[1]), int(split[2]), int(split[3])))

    # Get the answer for first part, form a set of possibilities for the opcodes
    total_sum = 0
    possibilities = {opcode : set() for opcode in range(16)}

    for i in range(len(before)):
        localsum = 0
        for operation in OPERATIONS:
            if operation(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
                localsum += 1
                possibilities[op[i][0]].add(operation)

        if localsum >= 3:
            total_sum += 1

    # Try to remove some possibilities by going through the instructions again
    for operation_code in possibilities:
        for i in range(len(before)):
            if op[i][0] == operation_code:
                prov = set()
                for operation in possibilities[operation_code]:
                    prov.add(operation)
                    if operation(op[i][1], op[i][2], op[i][3], list(before[i])) != list(after[i]):
                        prov.remove(operation)
                possibilities[operation_code] = set(x for x in prov)

    # Remove solved op codes from non solved op codes until all opcodes are solved
    removed = True
    while removed:
        removed = False
        for operation_code in possibilities:
            if len(possibilities[operation_code]) == 1:
                for op_cod in possibilities:
                    if op_cod != operation_code:
                        prov = set ()
                        for operation in possibilities[op_cod]:
                            prov.add(operation)
                            if operation in possibilities[operation_code]:
                                prov.remove(operation)
                                removed = True
                        possibilities[op_cod] = set(x for x in prov)

    return total_sum, possibilities


def solve2(codes):
    # Read the second part instructions, save data to a list
    program = []
    with open('input2') as f:
        for line in f.readlines():
            line = line.strip('\n')
            split = line.split(' ')
            program.append((int(split[0]), int(split[1]), int(split[2]), int(split[3])))

    # Intiate registers with 0 and let her rip
    regs = [0, 0, 0, 0]

    for instruction in program:
        for operation in codes[instruction[0]]:
            regs = operation(instruction[1], instruction[2], instruction[3], regs)

    return regs[0]


if __name__ == '__main__':
    main()
