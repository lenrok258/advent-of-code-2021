# test: 7
# input: 1548

lines = open('input.txt', 'r').read().splitlines()
input_numbers = list(map(lambda line: int(line), lines))

prv_num = None
result = 0
for cur_num in input_numbers:
    if prv_num and (cur_num - prv_num) > 0: 
        result += 1
    prv_num = cur_num

print(result)