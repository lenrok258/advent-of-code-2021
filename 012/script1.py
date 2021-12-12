from collections import defaultdict
from pprint import pprint
import re

# test: 
# input: 5333

lines = open('input.txt', 'r').read().splitlines()

doors = defaultdict(lambda: [])

for l in lines:
    door = l.split('-')
    doors[door[0]].append(door[1])
    doors[door[1]].append(door[0])


def is_small_cave(cave_name):
    return bool(re.match("^[a-z]*$", cave_name))


def travel(cave, path):
    path.append(cave)
    output_paths = []
    for ed in doors[cave]:
        if (ed in path) and is_small_cave(ed):
            continue;
        elif cave == 'end':
            return [path]
        else: 
            outputs = travel(ed, list(path))
            output_paths.extend(outputs)
    return output_paths


all_paths = travel("start", [])
print(len(all_paths))