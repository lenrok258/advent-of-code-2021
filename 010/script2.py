from collections import deque

# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

lefts = ['(', '[', '{', '<']
rights = [')', ']', '}', '>']
points = [1, 2, 3, 4]

inputs = []
for l in lines:
    inputs.append(list(l))

def print_inputs(inputs):
    for l in inputs:
        print("".join(l))

def is_left(charr):
    return True if charr in lefts else False

def remove_currupted(inputs):
    result = []
    for line in inputs:
        deq = deque()
        correct = True
        for c in list(line):
            if is_left(c):
                deq.append(c)
            else:
                left_companion = deq.pop()
                i = lefts.index(left_companion)
                if rights[i] != c:
                    pts = points[rights.index(c)]
                    correct = False
        if correct:
            result.append(line)
    return result

print_inputs(inputs)
inputs = remove_currupted(inputs)

print()
print_inputs(inputs)
print()

scores = []
for line in inputs:
    deq = deque()
    line_score = 0
    for c in list(line):
        if is_left(c):
            deq.append(c)
        else:
            left_companion = deq.pop()
            i = lefts.index(left_companion)
            if rights[i] != c:
                pts = points[rights.index(c)]
    for i in range(len(deq)):
        cc = deq.pop()
        line_score *= 5
        char_score = lefts.index(cc) + 1
        line_score += char_score
    scores.append(line_score)

print(scores)

scores = sorted(scores)
print(scores[len(scores)//2])