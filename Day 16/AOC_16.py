

def main():
    print_header()

    # Before, Op, After
    print(solve1(get_data()[0], get_data()[1], get_data()[2]))


def addr(a,b,c,regs):
    regs[c] = regs[a] + regs[b]
    return regs


def addi(a,b,c,regs):
    regs[c] = regs[a] + b
    return regs


def mulr(a,b,c,regs):
    regs[c]= regs[a] * regs[b]
    return regs


def muli(a,b,c,regs):
    regs[c] = regs[a] * b
    return regs


def banr(a,b,c,regs):
    regs[c] = regs[a] & regs[b]
    return regs


def bani(a,b,c,regs):
    regs[c] = regs[a] & b
    return regs


def borr(a,b,c,regs):
    regs[c] = regs[a] | regs[b]
    return regs


def bori(a,b,c,regs):
    regs[c] = regs[a] | b
    return regs


def setr(a,b,c,regs):
    regs[c] = regs[a]
    return regs


def seti(a,b,c,regs):
    regs[c] = a
    return regs


def gtir(a,b,c,regs):
    regs[c] = int(a > regs[b])
    return regs


def gtri(a,b,c,regs):
    regs[c] = int(regs[a] > b)
    return regs


def gtrr(a,b,c,regs):
    regs[c] = int(regs[a] > regs[b])
    return regs


def eqir(a,b,c,regs):
    regs[c] = int(a == regs[b])
    return regs


def eqri(a,b,c,regs):
    regs[c] = int(regs[a] == b)
    return regs


def eqrr(a,b,c,regs):
    regs[c] = int(regs[a] == regs[b])
    return regs


def get_data():
    before = []
    op = []
    after = []
    with open('input') as f:
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
    return before, op, after


def solve1(before, op, after):
    total_sum = 0

    for i in range(len(before)):
        localsum = 0
        if addr(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if addi(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if mulr(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if muli(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if banr(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if bani(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if borr(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if bori(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if setr(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if seti(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if gtir(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if gtri(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if gtrr(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if eqir(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if eqri(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1
        if eqrr(op[i][1], op[i][2], op[i][3], list(before[i])) == list(after[i]):
            localsum+=1

        if localsum >= 3:
            total_sum += 1

    return total_sum


def print_header():

    print("")
    print("######################################")
    print("####### Advent of code day 16 ########")
    print("######################################")
    print("")


if __name__ == '__main__':
    main()
