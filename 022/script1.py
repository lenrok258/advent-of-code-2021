from collections import defaultdict

# test: 
# input: 

lines = open('input_test.txt', 'r').read().splitlines()

instructions = []
for i,l  in enumerate(lines):
    enable = l.split(' ')[0]
    boundries = l.split(' ')[1].split(',')
    b_values = []
    for b in boundries:
        fromm, to = list(map(int, b.split('=')[1].split('..')))

        # normalize to 50x50x50
        if fromm <= -50:
            fromm = -50
        if to >= 50:
            to = 50

        b_values.extend([int(fromm), int(to + 1)])
    instructions.append([enable, *b_values])

print(instructions)

reactor = defaultdict(lambda :defaultdict(lambda :defaultdict(lambda:0)))

for inst in instructions:
    enable, x1, x2, y1, y2, z1, z2 = inst
    print(f"{inst}")
    for x in range(x1, x2):
        for y in range(y1, y2):
            for z in range(z1, z2):
                reactor[x][y][z] = 1 if enable == 'on' else 0

count = 0
for x in range(-50, 51):
    for y in range(-50, 51):
        for z in range(-50, 51):
            if reactor[x][y][z]:
                count += 1
            # print(reactor[x][y][z], end="")
print(count)
