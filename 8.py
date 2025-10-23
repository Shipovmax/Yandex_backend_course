from math import factorial as fact
from random import randrange as rnd


value = rnd(1,11)
result = fact(value)

print("Факториал", value, "равен", result)