# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

input_nums = list(map(int, lines[0].split(",")))

min_num = min(input_nums)
max_num = max(input_nums)

fuel_cost = [0] * (max_num + 1)
for step in range(1, max_num + 1):
    fuel_cost[step] = step + fuel_cost[step-1]

print(fuel_cost)

min_delta = 99999999999
delta = 0
for i in range(min_num, max_num + 1):
    # print(f"testing {i}")
    for num in input_nums:
        delta += fuel_cost[abs(num - i)]

    if delta < min_delta:
        min_delta = delta
    
    delta = 0


print(min_delta)