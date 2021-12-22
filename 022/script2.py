from typing import Optional, Tuple
from collections import Counter

# test: 474140, 2758514936282235
# input: 1268313839428137

lines = open('input.txt', 'r').read().splitlines()

instructions = []
for i,l  in enumerate(lines):
    enable = int(l.split(' ')[0] == 'on')
    boundries = l.split(' ')[1].split(',')
    b_values = []
    for b in boundries:
        fromm, to = list(map(int, b.split('=')[1].split('..')))
        b_values.extend([int(fromm), int(to)])
    instructions.append((enable, *b_values))


def intersect_segment(seg1, seg2) -> Optional[Tuple[int]]:
    s1x1, s1x2 = seg1
    s2x1, s2x2 = seg2
    # print(f"intersection {seg1}->{seg2} = {(max(s1x1, s2x1), min(s1x2, s2x2))}")
    if min(s1x2, s2x2) >= max(s1x1, s2x1):
        return (max(s1x1, s2x1), min(s1x2, s2x2))
    return None


def intersect_cubes(cube1, cube2):
    c1x1, c1x2, c1y1, c1y2, c1z1, c1z2 = cube1
    c2x1, c2x2, c2y1, c2y2, c2z1, c2z2 = cube2
    x_inse = intersect_segment((c1x1, c1x2), (c2x1, c2x2))
    y_inse = intersect_segment((c1y1, c1y2), (c2y1, c2y2))
    z_inse = intersect_segment((c1z1, c1z2), (c2z1, c2z2))
    if x_inse and y_inse and z_inse:
        return (x_inse[0], x_inse[1], y_inse[0], y_inse[1], z_inse[0], z_inse[1])


def cube_volume(cube):
    x1, x2, y1, y2, z1, z2 = cube
    return (x2-x1)*(y2-y1)*(z2-z1)


def toggle_cubes(step, cubes):
    state, cur = step[0], step[1:]
    new = Counter()
    for cube in cubes:
        intsct = intersect_cubes(cur, cube)
        if intsct:
            new[intsct] -= cubes[cube]
    if state:
        cubes[cur] = 1
    cubes.update(new)
    return cubes


def calc_toggled(cubes):
    res = 0
    for cube, how_many in cubes.items():
        x0, x1, y0, y1, z0, z1 = cube
        volume = (x1 + 1 - x0) * (y1 + 1 - y0) * (z1 + 1 - z0)
        res += volume * how_many
    return res


def reset_reactor(steps):
    cubes = Counter()
    for step in steps:
        cubes = toggle_cubes(step, cubes)
    return calc_toggled(cubes)


result = reset_reactor(instructions)
print(result) 