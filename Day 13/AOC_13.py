# UP = 0, LEFT = 1, DOWN = 2, RIGHT = 3
from header import print_header

DIRECTIONS = "^<v>"
DIRECTIONS_OPS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def main():
    print_header()
    data = get_data()
    print("Answer to part 1 is: {}".format(solve(data[0], data[1], True)))
    print("Answer to part 2 is: {}".format(solve(data[0], data[1])))


def take_second(elem):
    return elem[1]


def get_data():

    with open('input') as f:
        lines = f.readlines()

    tracks = [[*l.rstrip('\n')] for l in lines]
    carts = {}

    for y in range(len(tracks)):
        for x in range(len(tracks[y])):
            if tracks[y][x] in DIRECTIONS:
                carts[(x, y)] = (DIRECTIONS.index(tracks[y][x]), 0)

    # tracks will be an array with the initial state of the map
    # carts will be of [(x, y):(d,i)] where
    # x - is x position
    # y - is y position
    # d - is the direction the cart is facing, based on the index in DIRECTIONS
    # i - the number of times the cart turned in an intersection, initially 0
    return tracks, carts


def solve(tracks, carts, part1=False):
    while True:
        # Sort after every tick
        sorted_carts = sorted(carts, key=take_second)
        for cart in sorted_carts:
            x, y = cart
            d, i = carts.get(cart)
            x, y, d, i = move_cart(x, y, d, i, tracks)
            if (x, y) in carts:
                if part1:
                    return x, y
                del carts[cart]
                del carts[(x, y)]
                if (x, y) in sorted_carts:
                    sorted_carts.remove((x, y))
            else:
                del carts[cart]
                carts[(x, y)] = d, i

        if len(carts) == 1:
            for cart in carts:
                return cart


def move_cart(x, y, d, i, tracks):
    if tracks[y][x] in '|-':
        x, y = move(x, y, d)
        return x, y, d, i

    if tracks[y][x] == '+':
        i += 1

        # Reset index to such that we always have the first second third turn
        if i == 4:
            i = 1

        # Second turn is goes straight, so position does not change
        if i == 2:
            x, y = move(x, y, d)
            return x, y, d, i

        # First and third turn are left or right
        if i == 1 or i == 3:
            d = (d + i) % 4
            x, y = move(x, y, d)
            return x, y, d, i

    if tracks[y][x] == '/':
        # # UP = 0, LEFT = 1, DOWN = 2, RIGHT = 3
        # DIRECTIONS = "^<v>"
        d = [3, 2, 1, 0][d]
        x, y = move(x, y, d)
        return x, y, d, i

    if tracks[y][x] == '\\':
        # UP = 0, LEFT = 1, DOWN = 2, RIGHT = 3
        # DIRECTIONS = "^<v>"
        d = [1, 0, 3, 2][d]
        x, y = move(x, y, d)
        return x, y, d, i

    # If the track position is one where initially there was a cart, move along the way normally
    if tracks[y][x] in DIRECTIONS:
        x, y = move(x, y, d)
        return x, y, d, i


def move(x, y, d):
    delta = DIRECTIONS_OPS[d]
    x += delta[0]
    y += delta[1]
    return x, y


if __name__ == '__main__':
    main()
