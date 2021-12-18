# test: 
# input: 4457

import re

lines = open('input.txt', 'r').read().splitlines()


def create_expression(expression_string):
    return re.findall(r"\d+|[\[\]]", expression_string)


def find_pair_to_explode(expr):
    depth = 0
    prv_open_index = None
    for i, c in enumerate(expr):
        if c == '[':
            depth += 1
            prv_open_index = i
        if c == ']':
            depth -= 1
            if depth == 4:
                if str(expr[i-1]).isdigit() and str(expr[i-2]).isdigit():
                    return (i-2, i-1)
    return None


def find_num_to_split(expr):
    for i, c in enumerate(expr):
        if str(c).isdigit():
            digimon = int(c)
            if digimon > 9:
                return i


def add_expressions(expr_1, expr_2):
    return ['['] + expr_1 + expr_2 + [']']


def number_to_the_left(expr, start_idx):
    for i in range(1, start_idx):
        idx_to_test = start_idx - i
        if str(expr[idx_to_test]).isdigit():
            return idx_to_test
    return None
    

def number_to_the_right(expr, start_idx):
    idx_from, idx_to = start_idx + 1, len(expr)
    for i in range(idx_from, idx_to):
        if str(expr[i]).isdigit():
            return i
    return None


def explode(expr, num_to_explode):
    left_idx = num_to_explode[0]
    right_idx = num_to_explode[1]

    # numbers to explode
    a, b = int(expr[left_idx]), int(expr[right_idx])

    # find first digit to the left, add exploding num
    next_left_idx = number_to_the_left(expr, left_idx)
    if next_left_idx:
        old_value = int(expr[next_left_idx])
        expr[next_left_idx] = old_value + a

    # find first digit to the right, add exploding num
    next_right_idx = number_to_the_right(expr, right_idx)
    if next_right_idx:
        old_value = int(expr[next_right_idx])
        expr[next_right_idx] = old_value + b

    # replace exploding pair with 0
    return expr[:left_idx-1] + ['0'] + expr[right_idx+2:]


def split(expr, num_to_split_idx):
    split_me = int(expr[num_to_split_idx])
    floor = split_me // 2
    ceiling = split_me - floor
    els_to_add = ['[', floor, ceiling, ']']
    return expr[:num_to_split_idx] + els_to_add + expr[num_to_split_idx + 1:]


def reduce(expr):
    while True:
        pair_to_explode = find_pair_to_explode(expr)
        if pair_to_explode:
            expr = explode(expr, pair_to_explode)
            continue
        num_to_split_idx = find_num_to_split(expr)
        if num_to_split_idx:
            expr = split(expr, num_to_split_idx)
            continue
        break
    return expr


def compute_magnitude(expr):
    new_expr = list(expr)
    while len(new_expr) != 1:
        prv_e = None
        for i, e in enumerate(new_expr):
            if str(e).isdigit() and str(prv_e).isdigit():
                magn = 3*int(prv_e) + 2*int(e)
                temp_new_expr = new_expr[:i-1]
                if temp_new_expr[-1] == '[':
                    temp_new_expr = temp_new_expr[:-1]
                temp_new_expr.append(magn)
                rest = new_expr[i+1:]
                if rest[0] == ']':
                    rest = rest[1:]
                temp_new_expr.extend(rest)
                new_expr = temp_new_expr
                break
            prv_e = e
    return new_expr


expressions = []
for l in lines:
    expressions.append(create_expression(l))

prv_expr = None
for expr in expressions:
    if prv_expr:
        prv_expr = add_expressions(prv_expr, expr)
        prv_expr = reduce(prv_expr)
    else:
        prv_expr = expr

magnitude = compute_magnitude(prv_expr)
print(magnitude[0])