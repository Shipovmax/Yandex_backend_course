# Количество корзин с овощами, шт.
baskets = 462 
# Средний вес овощей в одной корзине, кг.
average_weight = 25
# Стоимость одного килограмма урожая, в монетах.
price_per_kg = 175 


# Допишите функцию, которая рассчитывает вес и стоимость урожая.
def calc( count_ca , ves_ovosh , who_mach ):
    resilts_ves = count_ca * ves_ovosh 
    results = resilts_ves * who_mach
    return resilts_ves , results

# Вызовите функцию calc() и обработайте вернувшееся значение.
a = calc(baskets , average_weight , price_per_kg)
# Составьте f-строку и напечатайте её.
print(f'Общий вес урожая: {a[0]} кг. Оценённая стоимость урожая: {a[1]}.')