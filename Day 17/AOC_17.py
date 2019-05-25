import collections
import sys

from header import print_header


def main():
    print_header()
    sys.setrecursionlimit(3000)
    clay = collections.defaultdict(bool)

    with open('input') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            a, depth = line.split(',')
            if a[0] == 'x':
                x = int(a.split('=')[1])
                y1 = int(depth.split('..')[0].split('=')[1])
                y2 = int(depth.split('..')[1])

                for y in range(y1, y2 + 1):
                    clay[(x, y)] = True

            else:
                y = int(a.split('=')[1])
                x1 = int(depth.split('..')[0].split('=')[1])
                x2 = int(depth.split('..')[1])

                for x in range(x1, x2 + 1):
                    clay[(x, y)] = True

    ymax = max(clay, key=lambda x: x[1])[1]

    def flow(clay, bottom):
        still, moving = set(), set()

        def traverse(p):
            if p in moving:
                return

            moving.add(p)

            x, y = p

            if y >= bottom:
                return False

            below = (x, y + 1)

            if below not in clay:
                traverse(below)

            if below not in clay and below not in still:
                return False

            left = (x - 1, y)
            right = (x + 1, y)

            left_finite = left in clay or traverse(left)
            right_finite = right in clay or traverse(right)

            if left_finite and right_finite:
                still.add(p)
                while left in moving:
                    still.add(left)
                    left = (left[0] - 1, y)
                while right in moving:
                    still.add(right)
                    right = (right[0] + 1, y)

            return left_finite or right_finite

        traverse((500, 0))
        return still, moving

    still, moving = flow(clay, ymax)
    print('Part 1: ' + str(len(moving)))
    print('Part 2: ' + str(len(still)))


if __name__ == '__main__':
    main()
