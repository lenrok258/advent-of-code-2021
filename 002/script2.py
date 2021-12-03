# test: 150
# input: 1864715580

lines = open('input.txt', 'r').read().splitlines()

hor_pos = 0
depth = 0
aim = 0

for l in lines:
    command_name, command_value = l.split()
    command_value = int(command_value)
    if command_name == 'forward':
        hor_pos += command_value
        depth += aim * command_value
    if command_name == 'down':
        aim += command_value
    if command_name == 'up':
        aim -= command_value

    print(f"{hor_pos} {depth} {aim}")

print(hor_pos)
print(depth)
print(hor_pos*depth)