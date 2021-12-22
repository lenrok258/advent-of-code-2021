from copy import copy
from functools import lru_cache

# test: 
# input: 712381680443927

lines = open('input.txt', 'r').read().splitlines()

starting_pos_1 = int(lines[0].split('Player 1 starting position: ')[1])
starting_pos_2 = int(lines[1].split('Player 2 starting position: ')[1])


def get_score(last_position, move):
    pos = last_position
    for i in range(move):
        pos += 1
        if pos > 10:
            pos = 1
    return pos


@lru_cache(maxsize=None)
def tick_3(player, p1_score, p2_score, p1_position, p2_position):

    print(f"{p1_score}")

    if p1_score >= 21:
        return [1, 0]
    elif p2_score >= 21:
        return [0, 1]

    prv_position = p1_position if player == 0 else p2_position

    wins = [0,0]
    for x in [1,2,3]:
        for y in [1,2,3]:
            for z in [1,2,3]:
                dice_result = x + y + z
                score = get_score(prv_position, dice_result)

                new_p1_score = p1_score
                new_p1_position = p1_position
                new_p2_score = p2_score
                new_p2_position = p2_position
                if player == 0:
                    new_p1_score = p1_score + score
                    new_p1_position = score
                elif player == 1:
                    new_p2_score = p2_score + score
                    new_p2_position = score

                next_player = 1 if player == 0 else 0
                single_res = tick_3(next_player, new_p1_score, new_p2_score, new_p1_position, new_p2_position)
                wins[0] += single_res[0]
                wins[1] += single_res[1]

    return wins

                
win_distribution = tick_3(0, 0, 0, starting_pos_1, starting_pos_2)
print(win_distribution)