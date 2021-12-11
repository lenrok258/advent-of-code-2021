# test: 1656
# input: 1757

lines = open('input.txt', 'r').read().splitlines()

cave = []
flash_count = 0

for l in lines:
    cave.append(list(map(int, list(l))))

h = len(cave)
w = len(cave[0])


def print_cave(cave):
    for y in cave:
        for x in y:
            if x == -1:
                print('*', end="")
            elif x == -2:
                print('.', end="")
            else:
                print(x, end="")
        print("")
    print("")


# (-1) -> about to flush
# (-2) -> flushed already in this step, don't touch
def inc_value(cave, x, y):
    val = cave[y][x]
    if val == 9:
        cave[y][x] = -1
    else:
        cave[y][x] += 1


def adjacents(cave, x, y):
    adjs = list()
    if (y > 0): adjs.append((x, y-1))
    if (y > 0 and x < w-1): adjs.append((x+1, y-1))
    if (x < w-1): adjs.append((x+1, y))
    if (x < w-1 and y < h-1): adjs.append((x+1, y+1))
    if (y < h-1): adjs.append((x, y+1))
    if (y < h-1 and x > 0): adjs.append((x-1, y+1))
    if (x > 0): adjs.append((x-1, y))
    if (y > 0 and x > 0): adjs.append((x-1, y-1))
    return adjs   
     

def get_flash_wannabe(cave):
    result = []
    for y in range(h):
        for x in range(w):
            if cave[y][x] == -1:
                result.append((x, y))
    return result


def flash(cave, x, y):
    global flash_count
    flash_count += 1

    cave[y][x] = -2
    adjs = adjacents(cave, x, y)
    for a in adjs:
        val = cave[a[1]][a[0]]
        if val == -1 or val == -2:
            continue
        inc_value(cave, a[0], a[1])
        
        if cave[a[1]][a[0]] == -1:
            flash(cave, a[0], a[1])


def tick(cave):
    # add one
    for y in range(h):
        for x in range(w):
            inc_value(cave, x, y)

    # flash candidates
    flash_them = get_flash_wannabe(cave)

    # flash 
    for e in flash_them:
        flash(cave, e[0], e[1])

    # set flashed in this tick to 0
    for y in range(h):
        for x in range(w):
            if cave[y][x] == -2:
                cave[y][x] = 0


print_cave(cave)
for i in range(100):
    print(f"step {i+1}:")
    tick(cave)
    print_cave(cave)

print(flash_count)