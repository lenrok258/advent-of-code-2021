# test: 198
# input: 3765399

def epsilon_on_position(iterable, position):
    counter_1 = 0
    for line in iterable:
        if line[position] == '1':
            counter_1 += 1
        
    counter_0 = len(iterable) - counter_1
    return '0' if counter_0 > counter_1 else '1'

lines = open('input.txt', 'r').read().splitlines()

oxygen_candidates= lines.copy()
co2_candidates = lines.copy()

numbers_len = len(lines[0])

for i in range(numbers_len):
    if len(oxygen_candidates) == 1:
        break
    g = epsilon_on_position(oxygen_candidates, i)
    for candidate in oxygen_candidates.copy():    
        if candidate[i] != g:
            oxygen_candidates.remove(candidate)

for i in range(numbers_len):
    if len(co2_candidates) == 1:
        break
    g = epsilon_on_position(co2_candidates, i)
    for candidate in co2_candidates.copy():
        if candidate[i] == g:
            co2_candidates.remove(candidate)

print(oxygen_candidates)
print(co2_candidates)

result = int(oxygen_candidates[0], 2) * int(co2_candidates[0], 2)
print(result)


    