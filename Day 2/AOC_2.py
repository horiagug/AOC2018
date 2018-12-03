from collections import Counter
from itertools import combinations


def main():
    print_header()

    #  Late at night, you sneak to the warehouse - who knows what kinds
    #  of paradoxes you could cause if you were discovered - and use
    #  your fancy wrist device to quickly scan every box and produce a
    #  list of the likely candidates (your puzzle input).

    #  To make sure you didn't miss any, you scan the likely candidate boxes
    #  again, counting the number that have an ID containing exactly two of
    #  any letter and then separately counting those with exactly three of
    #  any letter. You can multiply those two counts together to get a rudimentary
    #  checksum and compare it to what your device predicts.
    #  What is the checksum for your list of box IDs
    compute_checksum()

    #  Confident that your list of box IDs is complete, you're ready to find the
    #  boxes full of prototype fabric.

    #  The boxes will have IDs which differ by exactly one character at the same
    #  position in both strings.

    #  What letters are common between the two correct box IDs?
    common_box_id()


def print_header():
    print("")
    print("######################################")
    print("######## Advent of code day 2 ########")
    print("######################################")
    print("")


def compute_checksum():
    two_count = 0
    three_count = 0
    with open('input') as input_list:
        for line in input_list:
            counted_values = Counter(line).values()
            if 2 in  counted_values:
                two_count += 1
            if 3 in counted_values:
                three_count += 1
    checksum = two_count * three_count
    print(checksum)


def common_box_id():
    with open('input') as input_list:
        for a,b in combinations(input_list, 2):
            l = ''.join([x for x, y in zip(a, b) if x == y])
            if len(l) == len(a) - 1:
                print(l)


if __name__ == '__main__':
    main()
