# Пригодится для наполнения списков!
import random

# 1. Создание списка списков:
harvest = [[random.randint(5, 20) for _ in range(3)] for _ in range(3)]

# 2. Функция для подсчёта общего урожая:
def total_harvest(harvest_list):
    total = 0
    for plot in harvest_list:
        total += sum(plot)
    return total

# 3. Функция для подсчёта среднего урожая с каждого участка:
def average_harvest_per_plot(harvest_list):
    averages = []
    for plot in harvest_list:
        average = sum(plot) / len(plot)
        averages.append(average)
    return averages

# Вывод результатов
print('Урожай с каждой грядки на каждом участке:', harvest)
print('Общий урожай со всех участков:', total_harvest(harvest))
print('Средний урожай с каждого участка:', average_harvest_per_plot(harvest))