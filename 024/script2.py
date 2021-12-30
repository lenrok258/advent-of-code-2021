from collections import defaultdict, deque
from copy import copy
from functools import lru_cache
from itertools import product

# test: 
# input: 

boxes = [('u', 5), ('u', 9), ('u', 4), ('d', 12), ('u', 10), ('d', 13), ('d', 9), ('d', 12), ('u', 14), ('d', 9), ('u', 5), ('u', 10), ('d', 16), ('d', 2)]

possible_ups = product(range(1, 10), repeat = 7)

def test_serial(serial_ups):
    ups_deq = deque(serial_ups)
    z = 0

    serial = ""
    for box_type, box_v in boxes:
        if box_type == 'u':
            w = ups_deq.popleft()
            z = z * 26 + w + box_v
            serial += str(w)
        elif box_type == 'd':
            w = (z % 26) - box_v
            if w not in range(1,10):
                return None
            z = z // 26
            serial += str(w)
    
    # return None if not valid
    return serial if z == 0 else None


for n in possible_ups:
    result = test_serial(n)
    if result:
        print(result)
        break