# test: 5
# input: 6283

def print_board(board):
    for y in board:
        for x in y:
            print(x, end="")
        print("")


def draw_line(line, board):
    x1, y1 = map(int, line[0].split(","))
    x2, y2 = map(int, line[1].split(","))
    # print(f"{x1} {y1} -> {x2} {y2}")
    if x1 == x2:
        distance = abs(y1 - y2) + 1
        start_point = min(y1, y2)
        end_point = start_point + distance
        for i in range(start_point, end_point):
            board[i][x1] += 1
    elif y1 == y2:
        distance = abs(x1 - x2) + 1
        start_point = min(x1, x2)
        end_point = start_point + distance
        for i in range(start_point, end_point):
            board[y1][i] += 1


def compute_result(board):
    result = 0
    for y in board:
        for x in y:
            if int(x) > 1:
                result += 1
    return result


board_size = 10000
board  = [ [0] * board_size for i in range(board_size)]

lines = open('input.txt', 'r').read().splitlines()
vectors = list(map(lambda l: l.split(' -> '), lines))

# print(vectors)
for v in vectors:
    draw_line(v, board)

# print_board(board)

print(compute_result(board))

