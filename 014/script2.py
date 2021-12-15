from collections import defaultdict, Counter
import cProfile
from copy import copy

# test: 
# input: 4441317262452

lines = open('input.txt', 'r').read().splitlines()

tamplate = lines[0]
rules = {}
polymer = defaultdict(lambda: 0)
a_distribution = defaultdict(lambda: 0)

for l in lines[2:]:
    f, t = l.split(" -> ")
    rules[f] = t

# load template to polymer
for i, v in enumerate(tamplate):
    a_distribution[v] += 1
    if i > len(tamplate) - 2:
        break
    pair = "".join(tamplate[i:i+2])
    polymer[pair] += 1


def insertion_step(polymer, rules):
    new_polymer = copy(polymer)
    for rk, rv in rules.items():
        if polymer[rk]:
            seq_found = polymer[rk] 
            a_distribution[rv] += seq_found
            new_polymer[rk] -= seq_found
            new_key_1 = rk[0] + rv
            new_key_2 = rv + rk[1]
            new_polymer[new_key_1] += seq_found
            new_polymer[new_key_2] += seq_found
    return new_polymer


def calculate_new_polymer(polymer, rules, steps):
    new_polymer = copy(polymer)
    for i in range(steps):
        print(f"step {i}")
        new_polymer = insertion_step(new_polymer, rules)
    return new_polymer


calculate_new_polymer(polymer, rules, 40)

counter = Counter(a_distribution)
a_distr_sorted = counter.most_common()
a_max = a_distr_sorted[0][1]
a_min = a_distr_sorted[-1][1]

print(f"max:{a_max}, min:{a_min}")
print(a_max-a_min)