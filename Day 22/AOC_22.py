import networkx

from header import print_header

print_header()

target_x = 13
target_y = 726

depth = 3066


def geoindex_known(geoindex):
    # A region's erosion level is its geologic index plus the cave system's depth, all modulo 20183.
    e = (geoindex + depth) % 20183
    return e, e % 3


def generate_cave(target_x, target_y):
    cave = {}
    sum = 0
    for y in range(target_y + 1):
        for x in range(target_x + 1):
            if (x == 0 and y == 0) or (x == target_x and y == target_y):
                erosion, type = geoindex_known(0)

            elif y == 0:
                erosion, type = geoindex_known(x * 16807)

            elif x == 0:
                erosion, type = geoindex_known(y * 48271)

            else:
                erosion, type = geoindex_known(cave[(x-1, y)][0] * cave[(x, y-1)][0])

            cave[(x, y)] = erosion, type
            sum += cave[(x, y)][1]
    return cave, sum


print("Answer to part 1 is: {}".format(generate_cave(target_x, target_y)[1]))

rock, wet, narrow = 0, 1, 2
torch, gear, neither = 0, 1, 2

valid_items = {rock: (torch, gear), wet: (gear, neither), neither: (torch, neither)}
valid_regions = {torch: (rock, neither), gear: (rock, wet), neither: (wet, narrow)}


new_x = target_x + 100
new_y = target_y + 100

grid = {cord: tup[1] for cord, tup in (generate_cave(new_x, new_y))[0].items()}

graph = networkx.Graph()
for y in range(new_y + 1):
    for x in range(new_x + 1):
        items = valid_items[grid[(x, y)]]
        graph.add_edge((x, y, items[0]), (x, y, items[1]), weight=7)
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_x, next_y = x+dx, y+dy
            if 0 <= next_x <= new_x and 0 <= next_y <= new_y:
                new_items = valid_items[grid[(next_x, next_y)]]
                for item in set(items).intersection(set(new_items)):
                    graph.add_edge((x, y, item), (next_x, next_y, item), weight=1)

print("Answer to second part is: {}"
      .format(networkx.dijkstra_path_length(graph, (0, 0, torch), (target_x, target_y, torch))))
