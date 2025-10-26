# Вместо многоточия укажите необходимые параметры.
def count_tiles(depth, length, width=0):
    # Опишите условие, когда ширина бассейна не указана.
    if width == 0:
        width = length

    boot = length * width
    l_size = 2 * (depth * length)
    w_size = 2 * (depth * width)
    result = boot + l_size + w_size

    return result


total_tiles = count_tiles(1, 1)
print("Общее количество плиток для строительства бассейна:", total_tiles)
