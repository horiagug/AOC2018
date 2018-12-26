# As you see the Elves defend their hot chocolate successfully, you go back to falling through time. This is going to
#  become a problem.
#
# If you're ever going to return to your own time, you need to understand how this device on your wrist works. You
# have a little while before you reach your next destination, and with a bit of trial and error, you manage to pull
# up a programming manual on the device's tiny screen.
#
# According to the manual, the device has four registers (numbered 0 through 3) that can be manipulated by
# instructions containing one of 16 opcodes. The registers start with the value 0.
#
# Every instruction consists of four values: an opcode, two inputs (named A and B), and an output (named C),
# in that order. The opcode specifies the behavior of the instruction and how the inputs are interpreted. The output,
#  C, is always treated as a register.
#
# In the opcode descriptions below, if something says "value A", it means to take the number given as A literally. (
# This is also called an "immediate" value.) If something says "register A", it means to use the number given as A to
#  read from (or write to) the register with that number. So, if the opcode addi adds register A and value B,
# storing the result in register C, and the instruction addi 0 7 3 is encountered, it would add 7 to the value
# contained by register 0 and store the sum in register 3, never modifying registers 0, 1, or 2 in the process.
#
# Many opcodes are similar except for how they interpret their arguments. The opcodes fall into seven general
# categories:
#
# Addition:
#
#     addr (add register) stores into register C the result of adding register A and register B.
#     addi (add immediate) stores into register C the result of adding register A and value B.
#
# Multiplication:
#
#     mulr (multiply register) stores into register C the result of multiplying register A and register B.
#     muli (multiply immediate) stores into register C the result of multiplying register A and value B.
#
# Bitwise AND:
#
#     banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
#     bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
#
# Bitwise OR:
#
#     borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
#     bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
#
# Assignment:
#
#     setr (set register) copies the contents of register A into register C. (Input B is ignored.)
#     seti (set immediate) stores value A into register C. (Input B is ignored.)
#
# Greater-than testing:
#
# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise,
# register C is set to 0. gtri (greater-than register/immediate) sets register C to 1 if register A is greater than
# value B. Otherwise, register C is set to 0. gtrr (greater-than register/register) sets register C to 1 if register
# A is greater than register B. Otherwise, register C is set to 0.
#
# Equality testing:
#
# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is
# set to 0. eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise,
# register C is set to 0. eqrr (equal register/register) sets register C to 1 if register A is equal to register B.
# Otherwise, register C is set to 0.
#
# Unfortunately, while the manual gives the name of each opcode, it doesn't seem to indicate the number. However,
# you can monitor the CPU to see the contents of the registers before and after instructions are executed to try to
# work them out. Each opcode has a number from 0 through 15, but the manual doesn't say which is which. For example,
# suppose you capture the following sample:
#
# Before: [3, 2, 1, 1]
# 9 2 1 2
# After:  [3, 2, 2, 1]
#
# This sample shows the effect of the instruction 9 2 1 2 on the registers. Before the instruction is executed,
# register 0 has value 3, register 1 has value 2, and registers 2 and 3 have value 1. After the instruction is
# executed, register 2's value becomes 2.
#
# The instruction itself, 9 2 1 2, means that opcode 9 was executed with A=2, B=1, and C=2. Opcode 9 could be any of
# the 16 opcodes listed above, but only three of them behave in a way that would cause the result shown in the sample:
#
# Opcode 9 could be mulr: register 2 (which has a value of 1) times register 1 (which has a value of 2) produces 2,
# which matches the value stored in the output register, register 2. Opcode 9 could be addi: register 2 (which has a
# value of 1) plus value 1 produces 2, which matches the value stored in the output register, register 2. Opcode 9
# could be seti: value 2 matches the value stored in the output register, register 2; the number given for B is
# irrelevant.
#
# None of the other opcodes produce the result captured in the sample. Because of this, the sample above behaves like
#  three opcodes.
#
# You collect many of these samples (the first section of your puzzle input). The manual also includes a small test
# program (the second section of your puzzle input) - you can ignore it for now.
#
# Ignoring the opcode numbers, how many samples in your puzzle input behave like three or more opcodes?

# --- Part Two ---
#
# Using the samples you collected, work out the number of each opcode and execute the test program (the second
# section of your puzzle input).
#
# What value is contained in register 0 after executing the test program?


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

    # Try to remove some posibilities by going through the instructions again
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


def print_header():

    print("")
    print("######################################")
    print("####### Advent of code day 16 ########")
    print("######################################")
    print("")


if __name__ == '__main__':
    main()
