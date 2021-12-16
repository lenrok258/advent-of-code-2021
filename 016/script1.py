# test: 
# input: 955

lines = open('input.txt', 'r').read().splitlines()

input_hex = list(lines[0])

# The hexadecimal representation of this packet might encode a few extra 0 bits at the end; these are not part of the transmission and should be ignored.

def hex2bin(hex_char):
    return bin(int(hex_char, 16))[2:].rjust(4, '0')


def bin2dec(bin_value):
    return int(bin_value, 2)


def header_data_touple(bits):
    version_dec = bin2dec(bits[:3])
    type_dec = bin2dec(bits[3:6])
    value_bin = bits[6:]
    return ((version_dec, type_dec), value_bin)


def literal_value(bits):
    values = []
    bits_remaining = ""
    for i in range(9999999):
        value_segment_5bit = bits[5*i : 5 + 5*i]
        values.append(value_segment_5bit[1:])
        # the last segment
        if value_segment_5bit[0] == '0':
            bits_remaining = bits[5 + 5*i:]
            break
    literal = bin2dec("".join(values))
    return (literal, bits_remaining)


def typeid_data_touple(bits):
    # 0: next 15 bits: total length in bits of the sub-packets contained by this packet
    # 1: next 11 bits: number of sub-packets immediately contained by this packet.
    bit = bits[:1]
    type_id = 15 if bit == '0' else 11
    return (type_id, bits[1:])


def typevalue_data_touple(bits, typeid):
    typevalue_bin = bits[:typeid]
    typevalue_dec = bin2dec(typevalue_bin)
    return (typevalue_dec, bits[typeid:])


def process_package(bits):
    global ver_sum

    # at least 6 bits are required to decode header
    if len(bits) <= 6:
        return ""

    (ver, typ), data = header_data_touple(bits)
    ver_sum += ver

    if typ == 4: # literal
        literal, bits_remaining = literal_value(data)
        return bits_remaining

    if typ != 4: # operator
        typeid, data = typeid_data_touple(data)

        typevalue, data = typevalue_data_touple(data, typeid)

        if typeid == 15: # bit 0
            subpockets_bits_count = typevalue
            bits_to_process = data[:subpockets_bits_count]
            while bits_to_process:
                bits_to_process = process_package(bits_to_process)
            return data[subpockets_bits_count:]

        elif typeid == 11: # bit 1
            subpockets_count = typevalue
            bits_to_process = data
            for i in range(subpockets_count):
                bits_to_process = process_package(bits_to_process)
            return bits_to_process 


input_bin = "".join(list(map(lambda a: hex2bin(a), input_hex)))

ver_sum = 0
process_package(input_bin)
print(ver_sum)







