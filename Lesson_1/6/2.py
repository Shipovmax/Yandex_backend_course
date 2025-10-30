from random import randint 

# Начальная температура чая
current_temperature = 85

# Объявите цикл while
while current_temperature > 60 :
    minus = randint(1,3)
    current_temperature -= minus
    print(f'Прошла минута.')
    print(f'Чай остыл ещё на {minus} °C. Текущая температура: {current_temperature} °C')

print('Время пить чай!')