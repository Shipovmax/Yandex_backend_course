fruit_yields = [164.8, 105.0, 124.3, 113.8]  # Урожайность, кг на дерево.


corrected_fruit_yields = [yield_value + 1.2 for yield_value in fruit_yields]


print(corrected_fruit_yields)