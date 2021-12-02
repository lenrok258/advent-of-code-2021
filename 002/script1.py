# test: 150
# input: 

lines = open('input.txt', 'r').read().splitlines()

hor_pos = 0
depth = 0

for l in lines:
    command_name, command_value = l.split()
    if command_name == 'forward':
        hor_pos += int(command_value)
    if command_name == 'down':
        depth += int(command_value)
    if command_name == 'up':
        depth -= int(command_value);

print(hor_pos)
print(depth)
print(hor_pos*depth)