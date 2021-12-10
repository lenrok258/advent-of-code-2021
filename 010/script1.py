from collections import deque

# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

lefts = ['(', '[', '{', '<']
rights = [')', ']', '}', '>']
points = [3, 57, 1197, 25137]

def is_left(charr):
    return True if charr in lefts else False

result = 0

deque = deque()
for line in lines:
    for c in list(line):
        if is_left(c):
            deque.append(c)
        else:
            left_companion = deque.pop()
            i = lefts.index(left_companion)
            # print(f"right {c} {left_companion}")
            if rights[i] != c:
                pts = points[rights.index(c)]
                result += pts
                print(f"expected {rights[i]} but found {c} => {pts}pts")

print(result)