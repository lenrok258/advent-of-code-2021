# test: 198
# input: 

lines = open('input.txt', 'r').read().splitlines()

numbers_count = len(lines) 
counter_1 = [0] * len(lines[0])

gamma = ''
epsilon = ''

for line in lines:
    for i, digit in enumerate(line):
        if digit == '1':
            counter_1[i] += 1

for c1 in counter_1:
    count_1 = int(c1)
    count_0 = numbers_count - count_1
    if (count_0 >  count_1):
        gamma += '0'
    else:
        gamma += '1'

for c in gamma:
    if c == '1':
        epsilon += '0'
    else:
        epsilon += '1'

print(gamma)
print(epsilon)
print(int(gamma, 2))
print(int(epsilon, 2))
print(int(gamma, 2)*int(epsilon, 2))