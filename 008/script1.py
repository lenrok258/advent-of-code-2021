# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

signals = []
outputs = []
for l in lines:
    signals.append(l.split(' | ')[0].split())
    outputs.append(l.split(' | ')[1].split())

# print(signals)
# print(outputs)

result = 0
for o in outputs:
    for s in o:
        if len(s) in [2, 4, 3, 7]:
            print(len(s))
            result += 1

print(result)