from header import print_header


def main():
    print_header()

    fabric = {}
    input_lines = open('input').read().splitlines()

    p1 = compute_overlap(fabric, input_lines)
    print("The number of overlapped squares is: {}".format(p1))

    p2 = get_not_overlapping_id(fabric, input_lines)
    print("The ID of the non-overlapping cut is: {}".format(p2))


def get_indices(line):
    ls = line.split(' ')

    left = int(ls[2].split(',')[0])
    up = int(ls[2].split(',')[1][:-1])

    width = int(ls[3].split('x')[0])
    height = int(ls[3].split('x')[1])

    for i in range(up, up+height):
        for j in range(left, left+width):
            yield(i, j)


def compute_overlap(fabric, input_lines):
    for line in input_lines:
        for square in get_indices(line):
            if square in fabric:
                fabric[square] += 1
            else:
                fabric[square] = 1

    overlapped_squares = 0
    for var in fabric.values():
        if var >= 2:
            overlapped_squares += 1

    return overlapped_squares


def get_not_overlapping_id(fabric, input_lines):
    for line in input_lines:
        overlapped = False

        for square in get_indices(line):
            if fabric[square] != 1:
                overlapped = True

        if not overlapped:
            return line.split(' ')[0]


if __name__ == '__main__':
    main()
