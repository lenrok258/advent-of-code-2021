# test: 5
# input: 1589

lines = open('input.txt', 'r').read().splitlines()
input_numbers = list(map(lambda line: int(line), lines))

num_2, num_3, num_4 = None, None, None
result = 0
for num_1 in input_numbers:
    
    if num_2 and num_3 and num_4:
        window_1 = num_2 + num_3 + num_4
        window_2 = num_1 + num_2 + num_3
        if window_2 > window_1:
            print(f"{window_1} {window_2}")
            result += 1

    num_4 = num_3
    num_3 = num_2
    num_2 = num_1

    print(f"{num_1} {num_2} {num_3} {num_4}")

print(result)