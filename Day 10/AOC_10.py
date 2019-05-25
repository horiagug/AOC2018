from header import print_header


def main():
    print_header()

    get_word(get_data())


def get_data():
    points = []
    with open('input') as f:
        for line in f.readlines():
            line.strip(' ')
            x = int(line.split(', ')[0][10:])
            y = int(line.split(', ')[1].split('>')[0])
            vx = int(line.split('<')[2].split(', ')[0])
            vy = int(line.split('<')[2].split(', ')[1][:-2])
            points.append((list((x, y)), tuple((vx, vy))))

    return points


def printing_range(points):
    # Hardcoded values here, approximations to where something might start popping in the output
    for p in points:
        if p[0][0] not in range(-300, 300):
            return False
        elif p[0][1] not in range(-300, 300):
            return False
    return True


def print_grid(points):
    grid = []
    for p in points:
        grid.append((p[0][0], p[0][1]))

    temp = tuple(map(sorted, zip(*grid)))

    miny = temp[1][0]
    maxy = temp[1][-1]
    minx = temp[0][0]
    maxx = temp[0][-1]

    # min y point max y point
    for y in range(temp[1][0], temp[1][-1] + 1):
        out = '.'
        # min x point max x point
        for x in range(temp[0][0], temp[0][-1] + 1):
            if (x, y) in grid:
                out += '#'
            else:
                out += '.'
        print(out)

    return abs(maxx - minx), abs(maxy - miny)


def get_word(points):

    number_of_runs = 0
    exit = (10000000, 100000000)
    x = (10000000, 100000000)
    while True:

        # Round 'em up
        for p in points:
            p[0][0] += p[1][0]
            p[0][1] += p[1][1]

        if printing_range(points):
            x = print_grid(points)
            print(number_of_runs +1)

        if x < exit:
            exit = x
        elif x > exit:
            break

        number_of_runs += 1


if __name__ == '__main__':
    main()
