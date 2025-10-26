def count_tiles(depth, length, width=None):
    if width is None:
        width = length

    width_side = 2 * width * depth
    length_side = 2 * length * depth
    bottom_tiles = length * width
    total = width_side + length_side + bottom_tiles

    return total


def make_phrase(tiles_count):
    if tiles_count == 11 or tiles_count == 12 or tiles_count == 13 or tiles_count == 14:
        word = "плиток"
    elif tiles_count % 10 == 1:
        word = "плитку"
    elif tiles_count % 10 == 2 or tiles_count % 10 == 3 or tiles_count % 10 == 4:
        word = "плитки"
    else:
        word = "плиток"
    return str(tiles_count) + " " + word


total_tiles = count_tiles(2, 2, 2)
print("Для строительства бассейна нужно заготовить", str(make_phrase(total_tiles)))
