# Функция для создания словаря информации об овощах

def create_vegetable_info(list_1, list_2, list_3):
    list_2_3 = zip(list_2, list_3)
    vegetable_info = zip(list_1 , list_2_3)
    vegetable_info = dict(vegetable_info)
    return vegetable_info

# Тестовые данные:
vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
varieties = ['Красный куб', 'Аллигатор', 'Василёк', 'Тропический закат', 'Арктик']
yields = [6.5, 4.3, 2.8, 2.2, 3.5]

# Вызов функции:
print(create_vegetable_info(vegetables, varieties, yields))