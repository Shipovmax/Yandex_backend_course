# Овощи, которые растут в каждом из огородов
first_garden = {'помидоры', 'огурцы', 'морковь'}
second_garden = {'перец', 'помидоры', 'лук'}

set_1 = set(first_garden.split(' '))
set_2 = set(second_garden.split(' '))

# 1. Овощи, которые растут и в первом, и во втором огороде
common_vegetables = set.union(set_1, set_2)
print('Овощи, растущие и в первом, и во втором огороде:', common_vegetables)

# 2. Овощи, которые растут только в первом огороде
only_first_garden = 
print('Овощи, растущие только в первом огороде:', only_first_garden)

# 3. Овощи, которые растут только во втором огороде
only_second_garden = ...
print('Овощи, растущие только во втором огороде:', only_second_garden)