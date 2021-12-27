from copy import copy
from copy import deepcopy
from functools import lru_cache
from collections import defaultdict
from collections import deque

lines = open('input.txt', 'r').read().splitlines()

input_hallway = ('.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', '.')

input_rooms = (
    ('B', 'D', 'D', 'D',),
    ('A', 'C', 'B', 'C',),
    ('A', 'B', 'A', 'B',),
    ('D', 'A', 'C', 'C',),
)

# test values
# input_rooms = (
#     ('B', 'D', 'D', 'A',),
#     ('C', 'C', 'B', 'D',),
#     ('B', 'B', 'A', 'C',),
#     ('D', 'A', 'C', 'A',),
# )

def print_building(hallway, rooms):
    hallway_str = list(map(lambda h:h[0], hallway))
    print("".join(hallway_str))
    for i in range(4):
        print(f"  {rooms[0][i][0]} {rooms[1][i][0]} {rooms[2][i][0]} {rooms[3][i][0]}")
    print()


COST_MULTIPLIER = {'A':1, 'B':10, 'C':100, 'D':1000}
ROOM_NR_TO_EXIT_DOOR = [2,4,6,8]
ROOM_NR_TO_MATCHING_AMPH = ['A', 'B', 'C', 'D']
AMPH_TO_MARCHING_ROOM_NR = {'A':0, 'B':1, 'C':2, 'D':3}


def any_unmatching_amph_bellow(room, amph_i, matching_amph):
    for i in range(amph_i + 1, 4):
        if room[i] != matching_amph:
            return True
    return False


def get_room_empty_index_if_possible_to_enter(room, ampt_type):
    deepest_empty_spot = None
    for amph_i in range(0, 4):
        if room[amph_i] == '.':
            deepest_empty_spot = amph_i
    if deepest_empty_spot != None:
        if not any_unmatching_amph_bellow(room, deepest_empty_spot, ampt_type):
            return deepest_empty_spot
    return None


def hallway_empty_spots_indices(hallway):
    indices = []
    for i, s in enumerate(hallway):
        if s == '.':
            indices.append(i)
    return indices


def return_cost_if_path_possible(hallway, start_i, stop_i):
    assert hallway[stop_i] in ['.', 'X']

    step = 1 if start_i <= stop_i else -1
    range_start = start_i+1 if start_i <= stop_i else start_i-1
    range_end = stop_i+1 if start_i <= stop_i else stop_i-1
    cost = 0
    for i in range(range_start, range_end, step):
        if hallway[i] not in ['.', 'X']:
            return None
        cost += 1
    return cost


def move(hallway, rooms, hallway_i, hallway_v, room_i, amph_i, amph_v):
    new_hallway = list(copy(hallway))
    new_hallway[hallway_i] = hallway_v
    new_rooms = []
    for i, r in enumerate(rooms):
        new_room = list(copy(r))
        if i == room_i:
            new_room[amph_i] = amph_v
        new_rooms.append(tuple(new_room))
    return (tuple(new_hallway), tuple(new_rooms))


def moves_from_rooms_to_hallway(hallway, rooms):
    moves = []
    for room_i, room in enumerate(rooms):
        for amph_i, amph in enumerate(room):
            matching_amph = ROOM_NR_TO_MATCHING_AMPH[room_i]
            # empty space
            if amph == '.':
                continue
            # 1. can move it if in wrong room
            # 2. can move if in right room but unmatching ampth bellow
            if amph != matching_amph or (amph == matching_amph and any_unmatching_amph_bellow(room, amph_i, matching_amph)):
                exit_door = ROOM_NR_TO_EXIT_DOOR[room_i]
                for hallway_empty_spot_i in hallway_empty_spots_indices(hallway):
                    hallway_cost = return_cost_if_path_possible(hallway, exit_door, hallway_empty_spot_i)
                    if hallway_cost == None:
                        continue
                    new_hallway, new_rooms = move(hallway, rooms, hallway_empty_spot_i, amph, room_i, amph_i, '.')
                    cost = (amph_i + 1 + hallway_cost) * COST_MULTIPLIER[amph]
                    moves.append((new_hallway, new_rooms, cost))
                break
            # sanity check
            if amph == matching_amph and not any_unmatching_amph_bellow(room, amph_i, matching_amph):
                continue
            assert False
    return moves


def moves_from_hallway_to_rooms(hallway, rooms):
    moves = []
    for spot_i, spot in enumerate(hallway):
        if spot not in ['.', 'X']:
            amph = spot
            matching_room_nr = AMPH_TO_MARCHING_ROOM_NR[amph]
            exit_door_nr = ROOM_NR_TO_EXIT_DOOR[matching_room_nr]
            hallway_cost = return_cost_if_path_possible(hallway, spot_i, exit_door_nr)
            if hallway_cost == None:
                continue
            room = rooms[matching_room_nr]
            room_empty_i = get_room_empty_index_if_possible_to_enter(room, amph)
            if room_empty_i == None:
                continue
            new_hallway, new_rooms = move(hallway, rooms, spot_i, '.', matching_room_nr, room_empty_i, amph)
            cost = (hallway_cost + 1 + room_empty_i) * COST_MULTIPLIER[amph]
            moves.append((new_hallway, new_rooms, cost))
    return moves


@lru_cache(maxsize=None)
def all_possible_moves(hallway, rooms):
    moves = []
    moves_h2r = moves_from_hallway_to_rooms(hallway, rooms)
    moves_r2h = moves_from_rooms_to_hallway(hallway, rooms)
    moves.extend(moves_h2r)
    moves.extend(moves_r2h)
    return moves


def winnig_state(rooms):
    for room_i, room_v in enumerate(rooms):
        expected_amph_type = ROOM_NR_TO_MATCHING_AMPH[room_i]
        amphs_with_matching_type = list(filter(lambda a: a==expected_amph_type, room_v))
        if len(amphs_with_matching_type) != 4:
            return False
    return True


print_building(input_hallway, input_rooms)


# moves = all_possible_moves(input_hallway, input_rooms)
# for move in moves:
#     hallway, rooms, cost = move
#     print(f"cost: {cost}")
#     print_building(hallway, rooms)
# print()
# print(f"avilable moves: {len(moves)}")


def iterative_solution(hallway, rooms):
    moves = all_possible_moves(hallway, rooms)
    moves_to_check = deque()
    moves_to_check.extend(list(map(lambda m: (0, m), moves)))

    results_unique = set()
    min_result = 9999999999999
    for i in range(1_000_000):
        current_cost, (new_hallway, new_rooms, additional_cost) = moves_to_check.pop()
        new_cost = current_cost + additional_cost
        if winnig_state(new_rooms):
            min_result = min(min_result, new_cost)
            results_unique.add(new_cost)
        else:
            moves_to_add = all_possible_moves(new_hallway, new_rooms)
            moves_to_check.extend(list(map(lambda m: (new_cost, m), moves_to_add)))

        if (i % 10_000 == 0):
            print(f"{i} {len(moves_to_check)} {min_result}")
    return (min_result, results_unique)


# stats = defaultdict(lambda:0)

# @lru_cache(maxsize=None)
# def recursive_solution(hallway, rooms):
#     if winnig_state(rooms):
#         stats['winning'] += 1
#         return [0]
    
#     stats['tick'] += 1
#     if stats['tick'] % 10_000 == 0:
#         print(f"{stats['tick']} {stats['winning'] }")

#     all_possible_costs = []

#     moves = all_possible_moves(hallway, rooms)
#     for move in moves:
#         new_hallway, new_rooms, additional_cost = move
#         new_costs = recursive_solution(new_hallway, new_rooms)
#         all_possible_costs.extend(list(map(lambda c: c + additional_cost, new_costs)))

#     return all_possible_costs

min_result, results_unique = iterative_solution(input_hallway, input_rooms)
print(min_result)
print(f"Unique results = {results_unique}")

min_result = recursive_solution(input_hallway, input_rooms)
print(len(all_possible_costs))
print(min(all_possible_costs))
