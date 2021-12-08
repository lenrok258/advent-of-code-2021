import pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4)

# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

signals = []
outputs = []
for l in lines:
    signals.append(l.split(' | ')[0].split())
    outputs.append(l.split(' | ')[1].split())

def create_decoder(signals):
    decode_map_r = defaultdict(lambda: [])
    for sig in signals:
        if(len(sig) == 2):
            decode_map_r[1] = [sig]
        elif(len(sig) == 4):
            decode_map_r[4] = [sig]
        elif(len(sig) == 3):
            decode_map_r[7] = [sig]
        elif(len(sig) == 7):
            decode_map_r[8] = [sig]
        elif(len(sig) == 5):
            decode_map_r[2].append(sig)
            decode_map_r[3].append(sig)
            decode_map_r[5].append(sig)
        elif(len(sig) == 6):
            decode_map_r[6].append(sig)
            decode_map_r[9].append(sig)
            decode_map_r[0].append(sig)

    for v in decode_map_r[3]:
        if all(x in v for x in list(decode_map_r[1][0])):
            decode_map_r[3] = [v]
            for k in decode_map_r:
                if (k == 3):
                    continue
                if v in decode_map_r[k]: decode_map_r[k].remove(v)
    for v in decode_map_r[9]:
        if all(x in v for x in list(decode_map_r[4][0])):
            decode_map_r[9] = [v]
            for k in decode_map_r:
                if (k == 9):
                    continue
                if v in decode_map_r[k]: decode_map_r[k].remove(v)
    for v in decode_map_r[0]:
        if all(x in v for x in list(decode_map_r[7][0])):
            decode_map_r[0] = [v]
            for k in decode_map_r:
                if (k == 0):
                    continue
                if v in decode_map_r[k]: decode_map_r[k].remove(v)

    segment5 = set(decode_map_r[1][0]).intersection(list(decode_map_r[6][0]))
    segment5 = list(segment5)[0]

    for v in decode_map_r[5]:
        if segment5 in v:
            decode_map_r[5] = [v]
            for k in decode_map_r:
                if (k == 5):
                    continue
                if v in decode_map_r[k]: decode_map_r[k].remove(v)

    decoder_map = {}
    for k in decode_map_r:
        key_sorted = "".join(sorted(list(decode_map_r[k][0])))
        decoder_map[key_sorted] = k

    return decoder_map


def decode(decoder, secret):
    secret_sorted = "".join(sorted(list(secret)))
    return decoder[secret_sorted]


print(signals)
print(outputs)

result = 0
for i, s in enumerate(signals):
    decoder = create_decoder(s)
    
    result_chars = ""
    for o in outputs[i]:
        result_chars += str(decode(decoder, o))

    print(result_chars)
    result += int(result_chars)

print(result)
