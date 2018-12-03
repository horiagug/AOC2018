
def main():
    print_header()

# The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully
# wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still
# affecting them - nobody can even agree on how to cut the fabric.

# The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

# Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and
# consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined
#  as follows:

#    The number of inches between the left edge of the fabric and the left edge of the rectangle.
#    The number of inches between the top edge of the fabric and the top edge of the rectangle.
#    The width of the rectangle in inches.
#    The height of the rectangle in inches.

# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas.

# If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of
# fabric are within two or more claims?
    fabric = {}
    input_lines = open('input').read().splitlines()

    p1 = compute_overlap(fabric, input_lines)
    print("The number of overlapped squares is: {}".format(p1))

# Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any
# other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!
# What is the ID of the only claim that doesn't overlap?

    p2 = get_not_overlapping_id(fabric, input_lines)
    print("The ID of the non-overlapping cut is: {}".format(p2))


def print_header():
    print("")
    print("######################################")
    print("######## Advent of code day 3 ########")
    print("######################################")
    print("This is starting to get messy")
    print("######################################")
    print("")


def get_indices(line):
    ls = line.split(' ')

    left = int(ls[2].split(',')[0])
    up = int(ls[2].split(',')[1][:-1])

    width = int(ls[3].split('x')[0])
    height = int(ls[3].split('x')[1])

    for i in range (up, up+height):
        for j in range (left, left+width):
            yield(i,j)


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
