from copy import copy

# test: 
# input: 

lines = open('input_test.txt', 'r').read().splitlines()

starting_pos_1 = int(lines[0].split('Player 1 starting position: ')[1])
starting_pos_2 = int(lines[1].split('Player 2 starting position: ')[1])

print(f"{starting_pos_1}, {starting_pos_2}")

# return all posibilities
def roll_a_dice():
    return [1,2,3]
    # curr_value = dice_last_val
    # for i in range(3):
    #     curr_value += 1
    #     if curr_value > 21:
    #         curr_value = 1
    #     values.append(curr_value)
    # return values


def get_score(last_position, move):
    pos = last_position
    for i in range(move):
        pos += 1
        if pos > 10:
            pos = 1
    return pos


# def tick(player_no, players_scores, players_positions, dice_values):

#     dice_value = sum(dice_values)
#     score = get_score(players_positions[player_no], dice_value)
#     players_scores[player_no] += score
#     players_positions[player_no] = score

#     print(f"Player {player_no+1} rolls {dice_values} (sum: {dice_value}), got {score} points ({players_scores[player_no]})" )

#     if players_scores[player_no] >= 21:
#         print("We have a winner!")
#         return player_no

#     return None

def tick_2(player_no, players_scores, players_positions, dice_throw_no, player_dice_result):

    print(f"player: {player_no}, scores: {players_scores}, positions: {players_positions}, throw no: {dice_throw_no}, dice result {player_dice_result}")

    all_possible_rolls = roll_a_dice()

    all_possible_results = [0,0]
    for roll in all_possible_rolls:

        if dice_throw_no in [0,1]:
            
            dice_throw_no += 1
            roll_sum = player_dice_result + roll
            all_possible_results = tick_2(player_no, list(players_scores), list(players_positions), dice_throw_no, roll_sum)

        elif dice_throw_no in [2]:

            roll_sum = player_dice_result + roll

            score = get_score(players_positions[player_no], roll)
            players_scores[player_no] += score
            players_positions[player_no] = score
            if players_scores[player_no] >= 21:
                # dodaj do wyników
                if player_no == 0:
                    all_possible_results[0] += 1
                else:
                    all_possible_results[1] += 1
                continue
            
            # switch player
            new_player_no = 1 if player_no == 0 else 0
            # continue with the game with new player
            single_results = tick_2(new_player_no, list(players_scores), list(players_positions), 0, 0)
            # add computed results
            all_possible_results[0] += single_results[0]
            all_possible_results[1] += single_results[1]

        else:
            assert False

    return all_possible_results





# ------------------------

players_scores = [0] * 2
players_positions = [starting_pos_1, starting_pos_2]

winners_distribution = tick_2(0, players_scores, players_positions, 0, 0)

print(winners_distribution)