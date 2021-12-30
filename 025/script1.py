from collections import defaultdict
from copy import deepcopy

# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

input_map = defaultdict(lambda:defaultdict(lambda:'.'))
map_w, map_h = len(lines[0]), len(lines)
for l_i, l_v in enumerate(lines):
    for c_i, c_v in enumerate(list(l_v)):
        input_map[c_i][l_i] = c_v


def print_map(map):
    for y in range(map_h):
        for x in range(map_w):
            print(map[x][y], end="")
        print()
    print()


print_map(input_map)


def next_e_coor(x, y):
    return (x+1, y) if x+1 < map_w else (0, y)


def next_s_coor(x, y):
    return (x, y+1) if y+1 < map_h else (x, 0)


def tick(map):
    any_moves = False
    new_map = deepcopy(map)
    for y in range(map_h):
        for x in range(map_w):
            val = map[x][y]
            if val == '>':
                next_x, next_y = next_e_coor(x, y)
                # print(f"{x},{y} -> {next_x},{next_y}")
                if map[next_x][next_y] == '.':
                    new_map[x][y] = '.'
                    new_map[next_x][next_y] = '>'
                    any_moves = True
    new_new_map = deepcopy(new_map)
    for y in range(map_h):
        for x in range(map_w):
            val = new_map[x][y]
            if val == 'v':
                next_x, next_y = next_s_coor(x, y)
                if new_map[next_x][next_y] == '.':
                    new_new_map[x][y] = '.'
                    new_new_map[next_x][next_y] = 'v'
                    any_moves = True

    return (any_moves, new_new_map)

moves_count = 0
new_map = input_map
while True:
    any_moves, new_map = tick(new_map)
    # print_map(new_map)
    print(moves_count)
    if any_moves:
        moves_count += 1
    else:
        break
print(moves_count)