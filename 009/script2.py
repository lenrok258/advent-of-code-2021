# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

def print_cave(cave):
    for l in cave:
        print(l)

def get_adjacents(y, x, cave):
    adjacents = list()
    if (y > 0): adjacents.append(cave[y-1][x])
    if (x < len(cave[0])-1): adjacents.append(cave[y][x+1])
    if (y < len(cave)-1): adjacents.append(cave[y+1][x])
    if (x > 0): adjacents.append(cave[y][x-1])
    
    return adjacents

def check_if_local_min(y, x, cave, adjacents):
    val = cave[y][x]
    return True if val < min(adjacents) else False
    

cave = []
for l in lines:
    cave.append(list(map(int, list(l))))

def compute_low_points(cave):
    low_points = []
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            adjs = get_adjacents(y, x, cave)
            # print(f"{y}-{x}: {cave[y][x]} -> {adjs} {check_if_local_min(y, x, cave, adjs)}")
            if check_if_local_min(y, x, cave, adjs):
                low_points.append(cave[y][x])
    return low_points

low_points =compute_low_points(cave)
print(low_points)
low_points_plus_1 = list(map(lambda i: i+1,low_points))
print(low_points_plus_1)
print(sum(low_points_plus_1))
