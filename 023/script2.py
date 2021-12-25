from copy import copy
from copy import deepcopy
from functools import lru_cache
from collections import defaultdict

lines = open('input_test.txt', 'r').read().splitlines()

hallway = ('.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', '.')

rooms_list = [[],[],[],[]]
for i, l in enumerate(lines[2:6]):
    rooms_list[0].append((l[3], 0))
    rooms_list[1].append((l[5], 0))
    rooms_list[2].append((l[7], 0))
    rooms_list[3].append((l[9], 0))
rooms = (tuple(rooms_list[0]), tuple(rooms_list[1]), tuple(rooms_list[2]), tuple(rooms_list[3]) )
    
stats = defaultdict(lambda:0)

def print_building(hallway, rooms):
    hallway_str = list(map(lambda h:h[0], hallway))
    print("".join(hallway_str))
    for i in range(4):
        print(f"  {rooms[0][i][0]} {rooms[1][i][0]} {rooms[2][i][0]} {rooms[3][i][0]}")
    print()


def cost_multiplier(amph_type):
    return {'A':1, 'B':10, 'C':100, 'D':1000}[amph_type]


def ampth_type_to_room_nr(amph_type):
    return {'A':0, 'B':1, 'C':2, 'D':3}[amph_type]


print_building(hallway, rooms)

def is_final_state(rooms):
    # TODO: add checking if hallways is empty
    target_residents = ['A', 'B', 'C', 'D']
    for i, room in enumerate(rooms):
        room_set = set(list(map(lambda a:a[0], room)))
        if len(room_set) == 1 and list(room_set)[0] is target_residents[i]:
            continue
        else:
            return False
    return True


def room_to_hallway_position(room_nr):
    return [2, 4, 6, 8][room_nr]


def hallway_position_to_room_nr(hallway_pos):
    return [None,None,0,None,1,None,2,None,3,None,None][hallway_pos]


def copy_alter(hallway, rooms, room_nr, room_pos, room_new_value, hallway_pos, hallway_new_value):
    hallway_list = list(hallway)
    hallway_list[hallway_pos] = hallway_new_value
    new_hallway = tuple(hallway_list)

    rooms_list = []
    for room in rooms:
        room_list = list(room)
        rooms_list.append(room_list)
    rooms_list[room_nr][room_pos] = room_new_value
    new_rooms = (tuple(rooms_list[0]), tuple(rooms_list[1]), tuple(rooms_list[2]), tuple(rooms_list[3]))

    return (new_hallway, new_rooms)


def find_free_spot_in_room(room_nr, rooms, amph_type):
    room = rooms[room_nr]

    # If it is not your room, do not enter
    matching_room = ampth_type_to_room_nr(amph_type)
    if matching_room != room_nr:
        return None

    # If there is a wrong amph in the same room, do not go there or it will be blocked
    for spot_i in range(4):
        spot_v = room[spot_i]
        if spot_v != '.' and spot_v[0] != amph_type:
            return None

    # Look for the first one with '.' (empty space)
    for spot_i in reversed(range(4)): #3, 2, 1, 0
        spot_v = room[spot_i]
        if spot_v[0] == '.':
            return spot_i
   
    return None


# @lru_cache(maxsize=None)
def make_all_possible_moves(hallway, rooms):
    stats["tick"] += 1
    if stats["tick"] % 100_000 == 0:
        print(f"STATS: tick: {stats['tick']}, states checked: {stats['states_checked']}, no move: {stats['no_move']}, solusions: {stats['solution_found']}, current_min_solution: {stats['current_min_solution']}" ) 
        # print_building(hallway, rooms)

    states = []

    # move from hallway to room
    for hall_i, hall_v in enumerate(hallway):
        if hall_v in ['X', '.']:
            continue
        else:
            # go left
            for hallway_move in range(1, hall_i + 1):
                new_pos_candidate = hall_i - hallway_move
                if hallway[new_pos_candidate] == 'X':
                    room_nr = hallway_position_to_room_nr(new_pos_candidate)
                    free_spot_in_room = find_free_spot_in_room(room_nr, rooms, hall_v[0])
                    if free_spot_in_room == None:
                        continue
                    new_hallway, new_rooms = copy_alter(hallway, rooms, room_nr, free_spot_in_room, hall_v, hall_i, '.')
                    cost = (hallway_move + 1 + free_spot_in_room) * cost_multiplier(hall_v[0])
                    states.append((new_hallway, new_rooms, cost))
                elif hallway[new_pos_candidate] == '.':
                    continue
                else:
                    # someone stands on the way
                    break
            
            # go right
            for hallway_move in range(1, len(hallway)-hall_i):
                new_pos_candidate = hall_i + hallway_move
                if hallway[new_pos_candidate] == 'X':
                    room_nr = hallway_position_to_room_nr(new_pos_candidate)
                    free_spot_in_room = find_free_spot_in_room(room_nr, rooms, hall_v[0])
                    if free_spot_in_room == None:
                        continue
                    new_hallway, new_rooms = copy_alter(hallway, rooms, room_nr, free_spot_in_room, hall_v, hall_i, '.')
                    cost = (hallway_move + 1 + free_spot_in_room) * cost_multiplier(hall_v[0])
                    states.append((new_hallway, new_rooms, cost))
                elif hallway[new_pos_candidate] == '.':
                    continue
                else:
                    # someone stands on the way
                    break

    # move from room to hallway
    for room_nr, room in enumerate(rooms):
        for amph_i, amph in enumerate(room):
            # empty spot, try another amph in this room
            if amph[0] == '.':
                continue

            if amph[1] == 0: # 0 == not visited hallway yet
                room_halway_pos = room_to_hallway_position(room_nr)
                # move left
                for hallway_move in range(0, room_halway_pos):
                    hallway_position_candidate = room_halway_pos - 1 - hallway_move
                    
                    # not allowed to stand here
                    if hallway[hallway_position_candidate] == 'X':
                        continue

                    # valid move, create new game state and compute cost
                    elif hallway[hallway_position_candidate] == '.':
                        # create move
                        new_hallway, new_rooms = copy_alter(hallway, rooms, room_nr, amph_i, '.', hallway_position_candidate, (amph[0], 1))
                        cost = (1 + amph_i + 1 + hallway_move) * cost_multiplier(amph[0])
                        states.append((new_hallway, new_rooms, cost))
                    else: # some is already here
                        break

                # move right
                for hallway_move in range(0, len(hallway) - room_halway_pos - 1):
                    hallway_position_candidate = room_halway_pos + 1 + hallway_move
                    
                    # not allowed to stand here
                    if hallway[hallway_position_candidate] == 'X':
                        continue

                    # valid move, create new game state and compute cost
                    elif hallway[hallway_position_candidate] == '.':
                        # create move
                        new_hallway, new_rooms = copy_alter(hallway, rooms, room_nr, amph_i, '.', hallway_position_candidate, (amph[0], 1))
                        cost = (1 + amph_i + 1 + hallway_move) * cost_multiplier(amph[0])
                        states.append((new_hallway, new_rooms, cost))
                    else: # some is already here
                        break

            # only first one can move
            break

    if not states:
        stats["no_move"] += 1 
    
    stats["states_checked"] += len(states) 

    return tuple(states)


# @lru_cache(maxsize=None)
def tick(hallway, rooms, cost):
    if is_final_state(rooms):
        stats["solution_found"] += 1
        stats["current_min_solution"] = min(stats["current_min_solution"], cost)
        # print(f"Found solution!: {cost}")
        # print_building(hallway, rooms)
        return [cost]

    all_possible_costs = []
    for new_state in make_all_possible_moves(hallway, rooms):
        hallway, rooms, last_move_cost = new_state
        # print_building(hallway, rooms)
        new_costs = tick(hallway, rooms, cost + last_move_cost)
        all_possible_costs.extend(new_costs)
        # print(f"Path computed {all_possible_costs}")

    return all_possible_costs


# print(is_final_state(rooms))

# print(tick(hallway, rooms, 0))

# print(min(tick(hallway, rooms, 0)))

# moves = make_all_possible_moves(hallway, rooms)
# for move in moves:
#     hallway, rooms, cost = move
#     print(f"cost: {cost}")
#     print_building(hallway, rooms)
# print()
# print(f"avilable moves: {len(moves)}")

stats["current_min_solution"] = 9999999999999
result = tick(hallway, rooms, 0)
print(f"ALL POSSIBLE COSTS: {result}")
print(max(result))