from decimal import Decimal, getcontext
from math import pi

# Устанавливаем необходимую точность для вычислений
getcontext().prec = 10

pi = Decimal(str(pi))

# Длины полуосей эллипса
a = Decimal("2.5")
b = Decimal("1.75")


def find_ellipse_area(a, b):
    return pi * a * b


# Получаем площадь эллипса
area = find_ellipse_area(a, b)

# Глубина пруда
depth = Decimal("0.35")

# Объем воды: площадь * глубина
volume = area * depth

print(f"Площадь эллипса: {area} кв.м.")
print(f"Объём воды для наполнения пруда: {volume} куб.м.")
