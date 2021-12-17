# test: 
# input: 2326

lines = open('input.txt', 'r').read().splitlines()

trench_x, trench_y = lines[0].split('target area: x=')[1].split(', y=')
trench_x = list(map(int, trench_x.split('..')))
trench_y = list(map(int, trench_y.split('..')))
trench = (trench_x, trench_y)

print(f"trench: #{trench_x}# , #{trench_y}#\n")

def next_x(prv_x, init_vx, tick):
    if prv_x == None:
        return 0
    if tick == 1:
        return init_vx

    drag = (tick - 1)
    if init_vx - drag < 0:
        return prv_x 
    return prv_x + init_vx - drag


def next_y(prv_y, init_vy, tick):
    if prv_y == None:
        return 0
    if tick == 1:
        return init_vy

    gravity = -1 * (tick - 1)
    return prv_y + init_vy + gravity


def is_in_trench(point, trench):
    t_w, t_h = trench 
    x, y = point
    if x >= t_w[0] and x <= t_w[1]:
        if y >= t_h[0] and y <= t_h[1]:
            return True
    return False


def try_to_hit(init_vx, init_vy, ticks):
    prv_x = None
    prv_y = None
    for i in range(ticks):
        x = next_x(prv_x, init_vx, i)
        y = next_y(prv_y, init_vy, i)

        # one of coordiates is too far, break
        if x > trench[0][1] or y < trench[1][0]:
            return -1

        trech_hitted = is_in_trench((x, y), trench)

        if trech_hitted:
            return (x, y)    

        prv_x = x
        prv_y = y
    return -1


result = 0
for vx in range(0, 200):
    for vy in range(-200, 200):
        max_y = try_to_hit(vx, vy, 1000)
        if max_y != -1:
            result += 1


print(result)