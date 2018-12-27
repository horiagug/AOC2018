# You arrive in the year 18. If it weren't for the coat you got in 1018, you would be very cold: the North Pole base
# hasn't even been constructed.
#
# Rather, it hasn't been constructed yet. The Elves are making a little progress, but there's not a lot of liquid
# water in this climate, so they're getting very dehydrated. Maybe there's more underground?
#
# You scan a two-dimensional vertical slice of the ground nearby and discover that it is mostly sand with veins of
# clay. The scan only provides data with a granularity of square meters, but it should be good enough to determine
# how much water is trapped there. In the scan, x represents the distance to the right, and y represents the distance
#  down. There is also a spring of water near the surface at x=500, y=0. The scan identifies which square meters are
# clay (your puzzle input).
#
# For example, suppose your scan shows the following veins of clay:
#
# x=495, y=2..7
# y=7, x=495..501
# x=501, y=3..7
# x=498, y=2..4
# x=506, y=1..2
# x=498, y=10..13
# x=504, y=10..13
# y=13, x=498..504
#
# Rendering clay as #, sand as ., and the water spring as +, and with x increasing to the right and y increasing
# downward, this becomes:
#
#    44444455555555
#    99999900000000
#    45678901234567
#  0 ......+.......
#  1 ............#.
#  2 .#..#.......#.
#  3 .#..#..#......
#  4 .#..#..#......
#  5 .#.....#......
#  6 .#.....#......
#  7 .#######......
#  8 ..............
#  9 ..............
# 10 ....#.....#...
# 11 ....#.....#...
# 12 ....#.....#...
# 13 ....#######...
#
# The spring of water will produce water forever. Water can move through sand, but is blocked by clay. Water always
# moves down when possible, and spreads to the left and right otherwise, filling space that has clay on both sides
# and falling out otherwise.
#
# For example, if five squares of water are created, they will flow downward until they reach the clay and settle
# there. Water that has come to rest is shown here as ~, while sand through which water has passed (but which is now
# dry again) is shown as |:
#
# ......+.......
# ......|.....#.
# .#..#.|.....#.
# .#..#.|#......
# .#..#.|#......
# .#....|#......
# .#~~~~~#......
# .#######......
# ..............
# ..............
# ....#.....#...
# ....#.....#...
# ....#.....#...
# ....#######...
#
# Two squares of water can't occupy the same location. If another five squares of water are created, they will settle
#  on the first five, filling the clay reservoir a little more:
#
# ......+.......
# ......|.....#.
# .#..#.|.....#.
# .#..#.|#......
# .#..#.|#......
# .#~~~~~#......
# .#~~~~~#......
# .#######......
# ..............
# ..............
# ....#.....#...
# ....#.....#...
# ....#.....#...
# ....#######...
#
# Water pressure does not apply in this scenario. If another four squares of water are created, they will stay on the
#  right side of the barrier, and no water will reach the left side:
#
# ......+.......
# ......|.....#.
# .#..#.|.....#.
# .#..#~~#......
# .#..#~~#......
# .#~~~~~#......
# .#~~~~~#......
# .#######......
# ..............
# ..............
# ....#.....#...
# ....#.....#...
# ....#.....#...
# ....#######...
#
# At this point, the top reservoir overflows. While water can reach the tiles above the surface of the water,
# it cannot settle there, and so the next five squares of water settle like this:
#
# ......+.......
# ......|.....#.
# .#..#||||...#.
# .#..#~~#|.....
# .#..#~~#|.....
# .#~~~~~#|.....
# .#~~~~~#|.....
# .#######|.....
# ........|.....
# ........|.....
# ....#...|.#...
# ....#...|.#...
# ....#~~~~~#...
# ....#######...
#
# Note especially the leftmost |: the new squares of water can reach this tile, but cannot stop there. Instead,
# eventually, they all fall to the right and settle in the reservoir below.
#
# After 10 more squares of water, the bottom reservoir is also full:
#
# ......+.......
# ......|.....#.
# .#..#||||...#.
# .#..#~~#|.....
# .#..#~~#|.....
# .#~~~~~#|.....
# .#~~~~~#|.....
# .#######|.....
# ........|.....
# ........|.....
# ....#~~~~~#...
# ....#~~~~~#...
# ....#~~~~~#...
# ....#######...
#
# Finally, while there is nowhere left for the water to settle, it can reach a few more tiles before overflowing
# beyond the bottom of the scanned data:
#
# ......+.......    (line not counted: above minimum y value)
# ......|.....#.
# .#..#||||...#.
# .#..#~~#|.....
# .#..#~~#|.....
# .#~~~~~#|.....
# .#~~~~~#|.....
# .#######|.....
# ........|.....
# ...|||||||||..
# ...|#~~~~~#|..
# ...|#~~~~~#|..
# ...|#~~~~~#|..
# ...|#######|..
# ...|.......|..    (line not counted: below maximum y value)
# ...|.......|..    (line not counted: below maximum y value)
# ...|.......|..    (line not counted: below maximum y value)
#
# How many tiles can be reached by the water? To prevent counting forever, ignore tiles with a y coordinate smaller
# than the smallest y coordinate in your scan data or larger than the largest one. Any x coordinate is valid. In this
#  example, the lowest y coordinate given is 1, and the highest is 13, causing the water spring (in row 0) and the
# water falling off the bottom of the render (in rows 14 through infinity) to be ignored.
#
# So, in the example above, counting both water at rest (~) and other sand tiles the water can hypothetically reach (
# |), the total number of tiles the water can reach is 57.
#
# How many tiles can the water reach within the range of y values in your scan?

# --- Part Two ---
#
# After a very long time, the water spring will run dry. How much water will be retained?
#
# In the example above, water that won't eventually drain out is shown as ~, a total of 29 tiles.
#
# How many water tiles are left after the water spring stops producing water and all remaining water not at rest has
# drained?

import collections
import sys


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


def print_header():

    print("")
    print("######################################")
    print("####### Advent of code day 17 ########")
    print("######################################")
    print("")


if __name__ == '__main__':
    main()
