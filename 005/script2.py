# test: 12
# input: 18864

def print_board(board):
    for y in board:
        for x in y:
            print(x, end="")
        print("")


def draw_line(line, board):
    x1, y1 = map(int, line[0].split(","))
    x2, y2 = map(int, line[1].split(","))
    
    if x1 == x2:
        print(f"horizontal: {x1} {y1} -> {x2} {y2}")
        distance = abs(y1 - y2) + 1
        start_point = min(y1, y2)
        end_point = start_point + distance

        for i in range(start_point, end_point):
            board[i][x1] += 1
    
    elif y1 == y2:
        print(f"vertical: {x1} {y1} -> {x2} {y2}")
        distance = abs(x1 - x2) + 1
        start_point = min(x1, x2)
        end_point = start_point + distance

        for i in range(start_point, end_point):
            board[y1][i] += 1
    
    elif abs(x1 - x2) == abs(y1 - y2):
        print(f"45 deg: {x1} {y1} -> {x2} {y2}")
        x_direction = -1 if x1 > x2 else 1
        y_direction = -1 if y1 > y2 else 1
        distance = abs(x1 - x2) + 1

        for i in range(distance):
            x = x1 + (i * x_direction)
            y = y1 + (i * y_direction)
            board[y][x] +=1


def compute_result(board):
    result = 0
    for y in board:
        for x in y:
            if int(x) > 1:
                result += 1
    return result


board_size = 1000
board  = [ [0] * board_size for i in range(board_size) ]

lines = open('input.txt', 'r').read().splitlines()
vectors = list(map(lambda l: l.split(' -> '), lines))

for v in vectors:
    draw_line(v, board)

# print_board(board)

print(compute_result(board))

