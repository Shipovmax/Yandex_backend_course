def get_rectangle_area(length ,width):
    return length * width


def get_rectangle_perimeter(length ,width):
    return length * 2 + width * 2

# Длина прямоугольника.
length = 5
# Ширина прямоугольника.
width = 10


print("Площадь:", get_rectangle_area(length , width))
print("Периметр:", get_rectangle_perimeter(length , width))