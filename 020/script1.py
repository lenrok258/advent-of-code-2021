# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

infinity_char = '.'

enhancer = lines[0]
pic = []
for l in lines[2:]:
    pic.append(list(l))


def print_pic(pic):
    for l in pic:
        print("".join(l))
    print()


def resize_pic(pic, infinity_char):
    border_size = 5

    w = len(pic[0])
    empty_line = [infinity_char] * ( w + border_size*2 )

    result = []
    result.append(list(empty_line))
    result.append(list(empty_line))
    for l in pic:
        new_line = [infinity_char]*border_size + l + [infinity_char]*border_size
        result.append(new_line)
    result.append(list(empty_line))
    result.append(list(empty_line))

    return result


def empty_pic(pic, infinity_char):
    infinity_char = '#' if infinity_char == '.' else '.'
    w = len(pic[0])
    result = []
    empty_line = infinity_char * w
    for l in pic:
        result.append(list(empty_line))
    return result


def pixels_3x3(pic, point):        
    xp, yp = point
    result = []
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            value = pic[yp+y][xp+x]
            result.append(value)
    return result


def enhance_pixel(pic, enhancer, point):
    pixels = pixels_3x3(pic, point)
    pixels_s = "".join(pixels)
    pixels_bin = pixels_s.replace('.', '0').replace('#', '1')
    pixels_dec = int(pixels_bin, 2)

    # if point == (3,2):
    #     print(pixels_s)
    #     print(pixels_bin)
    #     print(pixels_dec)
    #     print(enhancer[pixels_dec])

    return enhancer[pixels_dec]


def enhance(pic, enhancer, infinity_char):
    # print_pic(pic)

    pic_resized = resize_pic(pic, infinity_char)
    pic_w, pic_h = len(pic_resized[0]), len(pic_resized)
    # print_pic(pic_resized)
    
    result = empty_pic(pic_resized, infinity_char)
    # print_pic(result)

    for y, line in enumerate(pic_resized[1:pic_h]):
        for x, p in enumerate(line[1:pic_w]):
            new_pix_val = enhance_pixel(pic_resized, enhancer, (x, y))
            result[y][x] = new_pix_val

    return result        


result = pic
print_pic(result)
for i in range(2):
    print(f"enhancing {i}")
    result = enhance(result, enhancer, infinity_char)
    print_pic(result)
    if enhancer[0] == '#':
        infinity_char = '#' if infinity_char == '.' else '.'

final_count = 0
for line in result:
    for c in line:
        if c == '#':
            final_count += 1
print(final_count)

