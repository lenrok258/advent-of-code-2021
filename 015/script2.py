from queue import PriorityQueue
from collections import defaultdict

# test: 
# input: 2844

lines = open('input.txt', 'r').read().splitlines()

cave = []

for l in lines:
    cave.append(list(map(int, list(l))))

cave_h = len(cave)
cave_w = len(cave[0])

x_directions = [0, 1, 0, -1]
y_directions = [1, 0, -1, 0]


def get_point_value(point):
    return cave[point[1]][point[0]]


def get_neighbors(point):
    neig = []
    x, y = point
    for s in range(4):
        new_x = x + x_directions[s]
        new_y = y + y_directions[s]
        if new_x >= 0 and new_x < cave_w:
            if new_y >= 0 and new_y < cave_h:
                neig.append((new_x, new_y))
    return neig


def inc_value(val, inc_step):
    for i in range(inc_step):
        val += 1
        if val > 9:
            val  = 1
    return val


def create_huge_cave(cave):
    new_cave = []
    for i, l in enumerate(cave):
        new_cave.append([])
        new_cave[i].extend(l)
        prv_line = l
        for j in range(4):
            new_line = list(map(lambda l:inc_value(l, 1), prv_line))
            new_cave[i].extend(new_line)
            prv_line = new_line
    new_cave_first_hori = list(new_cave)
    for kk in range(1, 5):
        next_segment = []
        for ll in new_cave_first_hori:
            nl = list(map(lambda aa:inc_value(aa, kk), ll))
            next_segment.append(nl)
        new_cave.extend(next_segment)
    return new_cave
        

def dijkstra(cave):
    cave_h, cave_w = len(cave), len(cave[0])
    pq = PriorityQueue()
    pq.put((0, (0, 0)))
    visited = {(0, 0)}
    while pq:
        curr_cost, (i, j) = pq.get()
        if i == cave_h - 1 and j == cave_w - 1:
            return curr_cost
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < cave_h and 0 <= y < cave_w and (x, y) not in visited:
                cost = cave[x][y]
                pq.put((curr_cost + cost, (x, y)))
                visited.add((x, y))


huge_cave = create_huge_cave(cave)
print(dijkstra(huge_cave))

