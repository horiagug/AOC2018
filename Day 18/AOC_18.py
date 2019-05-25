from header import print_header


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


if __name__ == '__main__':
    main()
