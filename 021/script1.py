# test: 
# input: 757770

lines = open('input.txt', 'r').read().splitlines()

starting_pos_1 = int(lines[0].split('Player 1 starting position: ')[1])
starting_pos_2 = int(lines[1].split('Player 2 starting position: ')[1])

print(f"{starting_pos_1}, {starting_pos_2}")


def roll_a_dice(dice_last_val):
    values = []
    curr_value = dice_last_val
    for i in range(3):
        curr_value += 1
        if curr_value > 100:
            curr_value = 1
        values.append(curr_value)
    return values


def get_score(last_position, move):
    pos = last_position
    for i in range(move):
        pos += 1
        if pos > 10:
            pos = 1
    return pos


def tick(player_no, players_scores, players_positions, dice_values):

    dice_value = sum(dice_values)
    score = get_score(players_positions[player_no], dice_value)
    players_scores[player_no] += score
    players_positions[player_no] = score

    print(f"Player {player_no+1} rolls {dice_values} (sum: {dice_value}), got {score} points ({players_scores[player_no]})" )

    if players_scores[player_no] >= 1000:
        print("We have a winner!")
        return player_no

    return None

# ------------------------

players_scores = [0] * 2
players_positions = [starting_pos_1, starting_pos_2]
dice_last_val = 0
dice_rolls = 0
active_player = 0

while True:
    dice_values = roll_a_dice(dice_last_val)
    dice_rolls += 3
    dice_last_val = dice_values[2]
    winner = tick(active_player, players_scores, players_positions, dice_values)
    if winner != None:
        break

    active_player = 1 if active_player == 0 else 0

    
looser = 1 if winner == 0 else 1
print(f"looser score {players_scores[looser]}, dice rolled {dice_rolls}")
print(players_scores[looser] * dice_rolls)