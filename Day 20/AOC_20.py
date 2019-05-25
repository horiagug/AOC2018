"""
Notes:

Map:
   Rooms are: .,
   Walls are: #
   Doors are: | or -   -> open left right or open up down
   Current position is: X

Regex:
    Start is ^
    End is $
    Branching is marked by |
    (NEWS|) means that the parenthesis can be skipped

"""
import networkx

from header import print_header


def main():
    regular_map = networkx.Graph()
    print_header()

    with open('input') as f:
        directions = f.readline()[1:-1]

    pos = {0}
    stack = []
    start, end = {0}, set()

    for step in directions:
        # 4 cases here:

        # Pipe means split in groups
        if step == "|":
            end.update(pos)
            pos = start

        # General direction
        elif step in "NSWE":
            direction = {'N': 1, 'S': -1, 'W': -1j, 'E': 1j}[step]
            regular_map.add_edges_from((p, p + direction) for p in pos)
            pos = {p + direction for p in pos}

        # Group starts in case of (
        elif step == '(':
            stack.append((start, end))
            start, end = pos, set()

        # Group ends in case of )
        elif step == ')':
            pos.update(end)
            start, end = stack.pop()

    lengths = networkx.algorithms.shortest_path_length(regular_map, 0)

    print('Answer to part 1 is: {}'.format(max(lengths.values())))
    print('Answer to part2 is: {}'.format(sum(1 for values in lengths.values() if values >= 1000)))


if __name__ == '__main__':
    main()
