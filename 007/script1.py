# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

input_nums = list(map(int, lines[0].split(",")))

min_num = min(input_nums)
max_num = max(input_nums)

min_delta = 99999999999
delta = 0
for i in range(min_num, max_num + 1):
    print(f"testing {i}")
    for num in input_nums:
        delta += abs(num - i)
    
    if delta < min_delta:
        min_delta = delta
    
    delta = 0


print(min_delta)