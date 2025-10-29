# Овощи, которые растут в каждом из огородов
first_garden = {"помидоры", "огурцы", "морковь"}
second_garden = {"перец", "помидоры", "лук"}

set_2 = second_garden
set_1 = first_garden

# 1. Овощи, которые растут и в первом, и во втором огороде
common_vegetables = set_1 & set_2
print("Овощи, растущие и в первом, и во втором огороде:", common_vegetables)

# 2. Овощи, которые растут только в первом огороде
only_first_garden = set.difference(set_1, set_2)
print("Овощи, растущие только в первом огороде:", only_first_garden)

# 3. Овощи, которые растут только во втором огороде
only_second_garden = set.difference(set_2, set_1)

print("Овощи, растущие только во втором огороде:", only_second_garden)
