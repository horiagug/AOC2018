from _operator import itemgetter
from collections import defaultdict

from header import print_header


def main():
    print_header()

    # Your puzzle input is 7403.

    grid = [[0 for x in range(301)] for y in range(301)]

    for y in range(1, 301):
        for x in range(1, 301):
            grid[x][y] = compute_power(7403, x, y)

    compute_puzzle(grid)


def compute_puzzle(grid):
    results = defaultdict(int)
    for size in range(1, 300):
        maxfound = 0
        for y in range(1, 301 - size):
            for x in range(1, 301 - size):
                cell_sum = 0
                for i in range(size):
                    for j in range(size):
                        cell_sum += grid[x + i][y + j]
                if cell_sum > maxfound:
                    results[(x,y,size)] += cell_sum

        print(max(results.items(), key=itemgetter(1))[0])


def compute_power(serial_number, x, y):
    rackID = x + 10
    pwr = rackID * y
    pwr += serial_number
    pwr *= rackID
    pwr = int(pwr / 100)
    return pwr % 10 - 5


if __name__ == '__main__':
    main()
