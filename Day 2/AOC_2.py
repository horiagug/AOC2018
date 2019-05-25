from collections import Counter
from itertools import combinations

from header import print_header


def main():
    print_header()

    compute_checksum()

    common_box_id()


def compute_checksum():
    two_count = 0
    three_count = 0
    with open('input') as input_list:
        for line in input_list:
            counted_values = Counter(line).values()
            if 2 in counted_values:
                two_count += 1
            if 3 in counted_values:
                three_count += 1
    checksum = two_count * three_count
    print(checksum)


def common_box_id():
    with open('input') as input_list:
        for a, b in combinations(input_list, 2):
            l = ''.join([x for x, y in zip(a, b) if x == y])
            if len(l) == len(a) - 1:
                print(l)


if __name__ == '__main__':
    main()
