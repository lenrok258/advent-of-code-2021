
from collections import defaultdict

# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

# at least 12 beacons

scanners = []

# loading 
beacons = []
scanner_no = None
for l in lines:
    if "---" in l:
        scanner_no = int(l.split('--- scanner ')[1].split(' ---')[0])
    elif not l:
        scanners.append(list(beacons))
        beacons = []
    else:
        beacons.append(list(map(int, l.split(','))))

# ---------------------

def possible_rotations():
    perm_x = {
        (1, 2, 3),
        (1, -3, 2),
        (1, -2, -3),
        (1, 3, -2),
    }

    perm_xy = set()
    for p in perm_x:
        perm_xy |= {
            p,
            (-p[2], p[1], p[0]),
            (-p[0], p[1], -p[2]),
            (p[2], p[1], -p[0]),
        }

    perm_xyz = set()
    for p in perm_xy:
        perm_xyz |= {
            p,
            (-p[1], p[0], p[2]),
            (-p[0], -p[1], p[2]),
            (p[1], -p[0], p[2]),
        }
    return perm_xyz


ROTATIONS = possible_rotations()

def rotate_point(point, rotation):
    new_x = point[abs(rotation[0])-1]
    new_y = point[abs(rotation[1])-1]
    new_z = point[abs(rotation[2])-1]
    if rotation[0] < 0:
        new_x = new_x * (-1)
    if rotation[1] < 0:
        new_y = new_y * (-1)
    if rotation[2] < 0:
        new_z = new_z * (-1)

    return (new_x, new_y,new_z)


def vector(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return (x1-x2, y1-y2, z1-z2)


def vector_and_rotation_if_overlapping(scanner1, scanner2):
    for rotation in ROTATIONS:
        distance_distribution = defaultdict(lambda: 0)
        for p1 in scanner1:
            for p2 in scanner2:
                p2_rotated = rotate_point(p2, rotation)
                vector_candidate = vector(p1, p2_rotated)
                distance_distribution[vector_candidate] += 1
        for k, v in distance_distribution.items():
            if v >= 12:
                print(f"OMG! Got it! vector:{k} share_points:{v} rotation:{rotation}")
                return (k, rotation)
    return (None, None)


def move_point_by_vector(point, vector):
    x, y, z = point
    vx, vy, vz = vector
    return (x+vx, y+vy, z+vz)


def translate_scanner(scanner, vector, rotation):
    scanner_translated = []
    for p in scanner:
        p_rotated = rotate_point(p, rotation)
        new_point = move_point_by_vector(p_rotated, vector)
        scanner_translated.append(new_point)
    return scanner_translated


scanners_translated = []
scanners_translated.append(scanners[0])

scanners_to_translate = list(scanners[1:])

while scanners_to_translate:
    for scanner in list(scanners_to_translate):
        for scanner_in_0 in list(scanners_translated):
            v, r = vector_and_rotation_if_overlapping(scanner_in_0, scanner)
            if v and r:
                translated = translate_scanner(scanner, v, r)
                scanners_translated.append(translated)
                scanners_to_translate.remove(scanner)
                break
            
beacons_unique = set()
for scanner in scanners_translated:
    for b in scanner:
        b_touple = (b[0], b[1], b[2])
        beacons_unique.add(b_touple)
print(len(beacons_unique))