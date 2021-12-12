from collections import defaultdict
from pprint import pprint
import cProfile

# test: 
# input: 146553

lines = open('input.txt', 'r').read().splitlines()

doors = defaultdict(lambda: [])

for l in lines:
    door = l.split('-')
    doors[door[0]].append(door[1])
    doors[door[1]].append(door[0])


def is_small_cave(cave_name):
    return cave_name.islower()


def travel(cave, path, small_cave_ticket):
    path.append(cave)
    output_paths = []
    for ed in doors[cave]:
        if ed == 'start':
            continue 
        elif is_small_cave(ed) and (ed in path) and not small_cave_ticket:
            continue
        elif cave == 'end':
            return [path]
        else: 
            new_small_cave_ticket = False if (is_small_cave(ed) and (ed in path)) else small_cave_ticket
            outputs = travel(ed, list(path), new_small_cave_ticket)
            output_paths.extend(outputs)
    return output_paths

# cProfile.run('travel("start", [], True)')

all_paths = travel("start", [], True)
print(len(all_paths))