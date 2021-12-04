# test: 1924
# input: 12738

import sys

def check_bingo(card):
    for x in range(5):
        for y in range(5):
            if card[x][y] != '-1':
                break
            if y == 4:
                return True
    for x in range(5):
        for y in range(5):
            if card[y][x] != '-1':
                break
            if y == 4:
                return True
    return False
 
def apply_number(number, card):
    for x, l in enumerate(card):
        for y, n in enumerate(l):
            if number == n:
                card[x][y] = '-1'

def print_cards(cards):
    for bc in cards:
        print("[")
        for l in bc:
            print("   ", end="")
            print(l)
        print("]")
        print(check_bingo(bc))
        print("")

def compute_result(card, number):
    result = 0
    for x, l in enumerate(card):
        for y, n in enumerate(l):
            if n != '-1':
                result += int(n)
    return result * int(number)

lines = open('input.txt', 'r').read().splitlines()

input_numbers = list(lines[0].split(','))
print(input_numbers)
print("")

bingo_cards = []

single_card = list()
for line in lines[2:]:

    if not line:
        bingo_cards.append(single_card)
        single_card = list()
        continue

    single_card.append(line.split())

# print_cards(bingo_cards)

for number in input_numbers:
    for card in bingo_cards.copy():
        apply_number(number, card)
        bingo = check_bingo(card)
        if bingo:
            print("---------- BINGO")
            print_cards(bingo_cards)
            if (len(bingo_cards) > 1):
                bingo_cards.remove(card)
            else:
                result = compute_result(card, number)
                print(result)
                sys.exit()
    



