from collections import defaultdict, deque
from copy import copy
from functools import lru_cache

# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

input_instr = []
for l in lines:
    instr = l.split(' ')[0]
    operands = l.split(' ')[1:]
    input_instr.append((instr, operands))


def get_val_b_value(val_b, register):
    if val_b.startswith('-'):
        return val_b
    return val_b if val_b.isdigit() else register[val_b]


def process_instr(instr, operands, register, input_deque):
    # print(f"{instr}\t{operands}   \t{list(input_deque)}\t   {dict(register)}")

    if instr == 'inp':
        var_a = operands[0]
        input_value = int(input_deque.popleft())
        register[var_a] = input_value
    elif instr == 'add':
        var_a, var_b = operands
        register[var_a] += int(get_val_b_value(var_b, register))
    elif instr == 'mul':
        var_a, var_b = operands
        register[var_a] *= int(get_val_b_value(var_b, register))
    elif instr == 'div':
        var_a, var_b = operands
        register[var_a] //= int(get_val_b_value(var_b, register))
    elif instr == 'mod':
        var_a, var_b = operands
        register[var_a] %= int(get_val_b_value(var_b, register))
    elif instr == 'eql':
        var_a, var_b = operands
        register[var_a] = 1 if register[var_a] == int(get_val_b_value(var_b, register)) else 0


def execute_nomad(program, input_deque, register_override={}):
    
    register = defaultdict(lambda : 0)
    register.update(register_override)
    
    for instr, operands in program:
        process_instr(instr, operands, register, input_deque)

    return register


def check_if_valid_serial(serial_string):
    input_deque = deque(serial_string)
    output_register = execute_nomad(input_instr, input_deque)
    return output_register['z'] == 0 

# -----------------------------

input_instr_grouped = []
group = []
for ii in input_instr:
    if ii[0] == 'inp':
        input_instr_grouped.append(copy(group))
        group = []
        group.append(ii)
    else:
        group.append(ii)
input_instr_grouped.append(group)

@lru_cache(maxsize=None)
def find_input_z_and_w(expected_output_z, digit_position_in_number):
    results = []
    for w in "123456789":
        for z in range(-20_000, 20_000):
            input_deque = deque(w)
            output_register = execute_nomad(input_instr_grouped[digit_position_in_number], input_deque, {'z':z})
            if output_register['z'] == expected_output_z:
                results.append((z, w))
    return results
            

@lru_cache(maxsize=None)
def recursion_magic(expected_output_z, digit_position_in_number):
    if digit_position_in_number == 0:
        if expected_output_z == 0:
            print("SOLUTOION HERE!")
            return ["S"]
        return ["X"]

    zw_list = find_input_z_and_w(expected_output_z, digit_position_in_number)
    if not zw_list:
        return ["X"]
    # print(f"{digit_position_in_number} {zw_list}")
    possible_results = []
    for zw in zw_list:
        zw_results = recursion_magic(zw[0], digit_position_in_number - 1)
        possible_results.extend(map(lambda res: str(zw[1]) + "-" + res, zw_results))

    # print(possible_results)   
    return possible_results


# solutions = recursion_magic(0, 14)
# solutions_int = list(map(lambda s: int(s.replace("-", "").replace("X", "")).replace("S", ""), solutions))
# solutions_int = list(filter(lambda a: a > 11111111111111), solutions_int)
# print(max(solutions_int))
# print(min(solutions_int))
# print(len(solutions_int))

# validation
# print(dict(execute_nomad(input_instr, deque("99919692496939"))))


def print_z_flow(input_s):
    override_z = 0
    input_deq = deque(input_s)
    z_s = ["0"]
    for program_segment in input_instr_grouped[1:]:
        output_reg = execute_nomad(program_segment, input_deq, {'z':override_z})
        override_z = output_reg['z']
        z_s.append(str(output_reg['z']))
    print("\t".join(z_s))

for i in range(15):
    print(f"{i}\t", end="")
print()
print()

print_z_flow("99919692496939")
print_z_flow("11111111111111")