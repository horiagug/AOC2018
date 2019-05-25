import collections

from header import print_header

print_header()

with open('input') as f:
    lines = f.readlines()


def get_cords(lines):
    points = []
    for line in lines:
        line.strip()
        x = int(line.split(", ")[0])
        y = int(line.split(", ")[1])
        points.append((x, y))
    return points


points = get_cords(lines)

ys = [min(y for _, y in points), max(y for _, y in points)]
xs = [min(x for x, _ in points), max(x for x, _ in points)]


def part_2(*p1):
    return 10000 > sum(m_dist(*p1, *p2) for p2 in points)


args = [(x, y) for y in range(*ys) for x in range(*xs)]


def part_1(*p1):
    table = {p2: m_dist(*p1, *p2) for p2 in points}
    point = min(table, key=table.get)
    if [*table.values()].count(table[point]) < 2:
        result[point] += 1


result = collections.defaultdict(int)


def m_dist(x, y, x1, y1):
    return abs(x1 - x) + abs(y1 - y)


[part_1(*p1) for p1 in args];

print('part 1:', max(result.values()));
print('part 2:', sum(1 for p1 in args if part_2(*p1)))
