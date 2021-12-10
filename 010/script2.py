from collections import deque

# test: 288957
# input: 3015539998

lines = open('input.txt', 'r').read().splitlines()

lefts = ['(', '[', '{', '<']
rights = [')', ']', '}', '>']

inputs = []
for l in lines:
    inputs.append(list(l))

def compute_scores(inputs):
    scores = []
    for line in inputs:
        deq = deque()
        correct = True
        for c in list(line):
            if c in lefts:
                deq.append(c)
            else:
                left_companion = deq.pop()
                i = lefts.index(left_companion)
                if rights[i] != c:
                    correct = False
        if correct:
            line_score = 0
            for i in range(len(deq)):
                cc = deq.pop()
                line_score = (line_score * 5) + lefts.index(cc) + 1
            scores.append(line_score)
    return scores

scores = compute_scores(inputs)

scores = sorted(scores)
print(scores[len(scores)//2])