def calculate_watering(plant_type, number_of_plants, volume_per_plant = 2.5):
    Number_of_waters = number_of_plants * volume_per_plant
    return print(str(plant_type), number_of_plants, "шт.:","для полива требуется", Number_of_waters , "л воды." )


# Вызов функции с позиционными аргументами:
calculate_watering('Артишоки', 20, 4)

# Вызов функции с позиционными аргументами, без опционального:
calculate_watering('Кивано', 15)

# Вызов функции с именованными аргументами, без опционального:
calculate_watering(number_of_plants=15, plant_type='Тыквы')