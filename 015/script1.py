from queue import PriorityQueue
from collections import defaultdict

# test: 
# input: 429

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


def dijkstra(cave):
    pq = PriorityQueue()
    cave_h, cave_w = len(cave), len(cave[0])
    starting_point = (0,0)
    pq.put((0, starting_point))
    visited = set(starting_point)
    while True:
        curr_cost, curr_point = pq.get()

        # cave exit
        if curr_point == (cave_w-1, cave_h-1):
            print(f"exit {curr_point} {curr_cost}")
            return curr_cost
        
        ns = get_neighbors(curr_point)
        for n in ns:
            if n not in visited:
                n_cost = get_point_value(n)
                pq.put((curr_cost + n_cost, n))
                visited.add(n)


dijkstra(cave)