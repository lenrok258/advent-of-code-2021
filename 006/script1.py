# test: 
# input: 

def print_distribution(day, distr):
    print(f"day {day} = ", end="")
    for f in distr.items():
        print(f"{f[1]} " , end="")
    print()

lines = open('input.txt', 'r').read().splitlines()

input = list(map(int, lines[0].split(',')))
days = 80

empty_distribution = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

fish_distribution = dict(empty_distribution)

for f in input:
    fish_distribution[f] += 1

print_distribution(0, fish_distribution)

for i in range(1, days+1):
    babies = fish_distribution[0] 
    for k in fish_distribution:
        if k == 0:
            continue
        fish_distribution[k-1] = fish_distribution[k]
    fish_distribution[8] = babies
    fish_distribution[6] += babies

    print_distribution(i, fish_distribution)

sum = 0
for i in fish_distribution:
    sum += fish_distribution[i]
print(sum)
        
