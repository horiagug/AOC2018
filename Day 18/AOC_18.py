# On the outskirts of the North Pole base construction project, many Elves are collecting lumber.
#
# The lumber collection area is 50 acres by 50 acres; each acre can be either open ground (.), trees (|),
# or a lumberyard (#). You take a scan of the area (your puzzle input).
#
# Strange magic is at work here: each minute, the landscape looks entirely different. In exactly one minute,
# an open acre can fill with trees, a wooded acre can be converted to a lumberyard, or a lumberyard can be cleared to
#  open ground (the lumber having been sent to other projects).
#
# The change to each acre is based entirely on the contents of that acre as well as the number of open, wooded,
# or lumberyard acres adjacent to it at the start of each minute. Here, "adjacent" means any of the eight acres
# surrounding that acre. (Acres on the edges of the lumber collection area might have fewer than eight adjacent
# acres; the missing acres aren't counted.)
#
# In particular:
#
# An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise,
# nothing happens. An acre filled with trees will become a lumberyard if three or more adjacent acres were
# lumberyards. Otherwise, nothing happens. An acre containing a lumberyard will remain a lumberyard if it was
# adjacent to at least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.
#
# These changes happen across all acres simultaneously, each of them using the state of all acres at the beginning of
#  the minute and changing to their new form by the end of that same minute. Changes that happen during the minute
# don't affect each other.
#
# For example, suppose the lumber collection area is instead only 10 by 10 acres with this initial configuration:
#
# Initial state:
# .#.#...|#.
# .....#|##|
# .|..|...#.
# ..|#.....#
# #.#|||#|#|
# ...#.||...
# .|....|...
# ||...#|.#|
# |.||||..|.
# ...#.|..|.
#
# After 1 minute:
# .......##.
# ......|###
# .|..|...#.
# ..|#||...#
# ..##||.|#|
# ...#||||..
# ||...|||..
# |||||.||.|
# ||||||||||
# ....||..|.
#
# After 2 minutes:
# .......#..
# ......|#..
# .|.|||....
# ..##|||..#
# ..###|||#|
# ...#|||||.
# |||||||||.
# ||||||||||
# ||||||||||
# .|||||||||
#
# After 3 minutes:
# .......#..
# ....|||#..
# .|.||||...
# ..###|||.#
# ...##|||#|
# .||##|||||
# ||||||||||
# ||||||||||
# ||||||||||
# ||||||||||
#
# After 4 minutes:
# .....|.#..
# ...||||#..
# .|.#||||..
# ..###||||#
# ...###||#|
# |||##|||||
# ||||||||||
# ||||||||||
# ||||||||||
# ||||||||||
#
# After 5 minutes:
# ....|||#..
# ...||||#..
# .|.##||||.
# ..####|||#
# .|.###||#|
# |||###||||
# ||||||||||
# ||||||||||
# ||||||||||
# ||||||||||
#
# After 6 minutes:
# ...||||#..
# ...||||#..
# .|.###|||.
# ..#.##|||#
# |||#.##|#|
# |||###||||
# ||||#|||||
# ||||||||||
# ||||||||||
# ||||||||||
#
# After 7 minutes:
# ...||||#..
# ..||#|##..
# .|.####||.
# ||#..##||#
# ||##.##|#|
# |||####|||
# |||###||||
# ||||||||||
# ||||||||||
# ||||||||||
#
# After 8 minutes:
# ..||||##..
# ..|#####..
# |||#####|.
# ||#...##|#
# ||##..###|
# ||##.###||
# |||####|||
# ||||#|||||
# ||||||||||
# ||||||||||
#
# After 9 minutes:
# ..||###...
# .||#####..
# ||##...##.
# ||#....###
# |##....##|
# ||##..###|
# ||######||
# |||###||||
# ||||||||||
# ||||||||||
#
# After 10 minutes:
# .||##.....
# ||###.....
# ||##......
# |##.....##
# |##.....##
# |##....##|
# ||##.####|
# ||#####|||
# ||||#|||||
# ||||||||||
#
# After 10 minutes, there are 37 wooded acres and 31 lumberyards. Multiplying the number of wooded acres by the
# number of lumberyards gives the total resource value after ten minutes: 37 * 31 = 1147.
#
# What will the total resource value of the lumber collection area be after 10 minutes?
#
# --- Part Two ---
#
# This important natural resource will need to last for at least thousands of years. Are the Elves collecting this
# lumber sustainably?
#
# What will the total resource value of the lumber collection area be after 1000000000 minutes?


def main():
    print_header()

    with open('input') as f:
        lines = f.readlines()

        grid = [['.'for x in range(len(lines[0]) -1)] for y in range(len(lines))]

        for x in range(len(lines[0]) - 1):
            for y in range(len(lines)):
                grid[x][y] = lines[x][y]

    def check(grid, x, y, dx, dy, string):
        x1 = x + dx
        y1 = y + dy

        if 0 <= x1 <= 49 and 0 <= y1 <= 49:
            if grid[x1][y1] == string:
                return 1
        return 0

    def production(minutes, grid):
        prevs = []

        for i in range(1, minutes + 1):
            new_grid = [['.' for x in range(len(lines[0]) - 1)] for y in range(len(lines))]
            for x in range(len(lines[0]) - 1):
                for y in range(len(lines)):

                    # Open
                    if grid[x][y] == '.':
                        number = 0
                        for dx in range(-1, 2):
                            for dy in range(-1, 2):
                                if dx == 0 and dy == 0:
                                    continue
                                number += check(grid, x, y, dx, dy, '|')
                        if number >= 3:
                            new_grid[x][y] = '|'
                        else:
                            new_grid[x][y] = '.'

                    # Tree
                    if grid[x][y] == '|':
                        number = 0
                        for dx in range(-1, 2):
                            for dy in range(-1, 2):
                                if dx == 0 and dy == 0:
                                    continue
                                number += check(grid, x, y, dx, dy, '#')
                        if number >= 3:
                            new_grid[x][y] = '#'
                        else:
                            new_grid[x][y] = '|'

                    # Lumber
                    if grid[x][y] == '#':
                        number_lumber = 0
                        number_trees = 0
                        for dx in range(-1, 2):
                            for dy in range(-1, 2):
                                if dx == 0 and dy == 0:
                                    continue
                                number_lumber += check(grid, x, y, dx, dy, '#')
                                number_trees += check(grid, x, y, dx, dy, '|')
                        if number_lumber >= 1 and number_trees >= 1:
                            new_grid[x][y] = '#'
                        else:
                            new_grid[x][y] = '.'
            grid = new_grid

            prev = '\n'.join(''.join(row) for row in grid)

            # Check for patterns return if found
            if prev in prevs:
                rep = prevs.index(prev)
                print('Found Pattern: {} is a repeat of: {}'.format(rep, i))
                period = i - (1 + rep)
                while (rep+1) % period != minutes % period:
                    rep += 1
                number_lumber = prevs[rep].count('#')
                number_trees = prevs[rep].count('|')
                return number_lumber * number_trees

            prevs.append(prev)

        number_lumber = 0
        number_trees = 0
        for x in range(len(lines[0]) - 1):
                number_lumber += grid[x].count("#")
                number_trees += grid[x].count('|')

        return number_lumber * number_trees

    print("Answer to part 1 is: " + str(production(10, grid)))
    print("Answer to second part is: " + str(production(1000000000, grid)))


def print_header():

    print("")
    print("######################################")
    print("####### Advent of code day 18 ########")
    print("######################################")
    print("")


if __name__ == '__main__':
    main()
