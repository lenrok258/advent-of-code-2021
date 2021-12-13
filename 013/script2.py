# test: O
# input: KJBKEUBG

lines = open('input.txt', 'r').read().splitlines()

dots = []
folds = []

loading_dots = True
for l in lines:
    if not l:
        loading_dots = False
        continue;
    if loading_dots:
        x,y = map(int, l.split(','))
        dots.append((x, y))
    else:
        axis, value = l.split("fold along ")[1].split("=")
        folds.append((axis, int(value)))


def fold(dots, axis, fold_position):
    new_dots = list(dots)
    for d in dots:
        x, y = d
        if axis == 'y':
            if y > fold_position:
                new_y = fold_position - (y - fold_position)
                new_dots.append((x, new_y))
                new_dots.remove(d)
        if axis == 'x':
            if x > fold_position:
                new_x = fold_position - (x - fold_position)
                new_dots.append((new_x, y))
                new_dots.remove(d)
    return list(set(new_dots))

folded_dots = list(dots)
for f in folds:
    folded_dots = fold(folded_dots, f[0], f[1])

max_x = max(map(lambda f: f[0], folded_dots)) + 1
max_y = max(map(lambda f: f[1], folded_dots)) + 1

paper_size = max(max_x, max_y)
printer = [['.'] * paper_size for i in range(paper_size)]

for d in folded_dots:
    x, y = d
    if x < paper_size and y < paper_size:
        printer[y][x] = '#'

for l in printer:
    for p in l:
        print(p, end="")
    print() 
