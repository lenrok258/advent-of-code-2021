import math

# test: 1134
# input: 858494

lines = open('input.txt', 'r').read().splitlines()

cave = []
for l in lines:
    cave.append(list(map(int, list(l))))

def clone_cave(cave):
    clone = []
    for l in cave:
        clone.append(list(l))
    return clone

def print_cave(cave):
    for l in cave:
        print(l)

def get_value(cave, xy_touple):
    return cave[xy_touple[1]][xy_touple[0]]

def get_adjacents(x, y, cave):
    adjacents = list()
    if (y > 0): adjacents.append((x, y-1))
    if (x < len(cave[0])-1): adjacents.append((x+1, y))
    if (y < len(cave)-1): adjacents.append((x, y+1))
    if (x > 0): adjacents.append((x-1, y))
    return adjacents

def check_if_local_min(y, x, cave, adjacents):
    val = cave[y][x]
    adjs_vals = list(map(lambda a: get_value(cave, a), adjacents))
    return True if val < min(adjs_vals) else False

def compute_low_points(cave):
    low_points = []
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            adjs = get_adjacents(x, y, cave)
            # print(f"{y}-{x}: {cave[y][x]} -> {adjs} {check_if_local_min(y, x, cave, adjs)}")
            if check_if_local_min(y, x, cave, adjs):
                low_points.append((x,y))
    return low_points


def compute_basin(cave, x, y):
    print(f"basin {x}-{y}")
    result = set()
    result.add((x, y))

    val = cave[y][x]
    adjs = get_adjacents(x, y, cave)
    adjs_lesser = list(filter(lambda a: get_value(cave, a) > val and get_value(cave, a) != 9, adjs))
    print(f"adj lesser = {adjs_lesser}")
    if not adjs_lesser:
        return result
    for al in adjs_lesser:
        result.update(compute_basin(cave, al[0], al[1]))
    return result
    
basins_sizes = []
low_points = compute_low_points(cave)
for lw in low_points:
    basin_points = compute_basin(clone_cave(cave), lw[0], lw[1])
    basins_sizes.append(len(basin_points))

# basin_points = compute_basin(clone_cave(cave), 6, 4)
basins_sizes = sorted(basins_sizes, reverse=True)

print(basins_sizes)
print(math.prod(basins_sizes[:3]))


