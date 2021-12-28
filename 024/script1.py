from collections import defaultdict, deque

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


def execute_nomad(program, input_deque, register_override):
    
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

# tick = 0
# for serial_candidate in range(99999999999999, 11111111111111, -1):
    pass
    # serial_candidate = str(serial_candidate)
    # if '0' in serial_candidate:
    #     continue

    # valid = check_if_valid_serial(serial_candidate)
    # if (valid):
    #     print(serial_candidate)
    #     break

    # tick += 1
    # if tick % 100_000 == 0:
    #     print(tick)

# print(check_if_valid_serial("13579246899999"))

for w in "123456789":
    for z in range(0, 100):
        input_deque = deque(w)
        output_register = execute_nomad(input_instr[216:234], input_deque, {'z':z})
        if output_register['z'] == 10:
            print(f"z zero dla input z {z} i w = {w}")
        # print(dict(output_register))

print("============")


