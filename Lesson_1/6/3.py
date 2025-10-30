fruit_yields = [164.8, 105.0, 124.3, 113.8]  # Урожайность, кг на дерево.

corrected_fruit_yields = []

for fruit in fruit_yields:
    corrected_fruit_yields.append(fruit + 1.2)
    
print(corrected_fruit_yields)