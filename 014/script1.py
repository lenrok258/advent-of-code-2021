from collections import deque
from collections import defaultdict

# test: 
# input: 3906

lines = open('input.txt', 'r').read().splitlines()

tamplate = lines[0]
rules = {}
polymer = deque(list(tamplate))

for l in lines[2:]:
    f, t = l.split(" -> ")
    rules[f] = t


def insertion_step(polymer, rules):
    new_polymer = deque()
    while len(polymer) > 1:
        a = polymer.popleft()
        b = polymer[0]
        new_polymer.append(a)
        if a + b in rules:
            new_polymer.append(rules[a + b])
    new_polymer.append(polymer[0])
    return new_polymer


new_polymer = deque(polymer)
for i in range(10):
    new_polymer = insertion_step(new_polymer, rules)

a_distribution = defaultdict(lambda: 0)
for a in new_polymer:
    a_distribution[a] += 1

a_distr_sorted = sorted(a_distribution, key=a_distribution.get, reverse=True)
a_max = a_distribution[a_distr_sorted[0]]
a_min = a_distribution[a_distr_sorted[-1]]

print(f"max:{a_max}, min:{a_min}")
print(a_max-a_min)
