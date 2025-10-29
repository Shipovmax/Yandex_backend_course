def get_stickers_comparison(collection_1, collection_2):
    set_1 = set(collection_1)
    set_2 = set(collection_2)

    # Находим уникальные элементы для каждой коллекции и общие элементы
    unique_1 = set_1 - set_2
    unique_2 = set_2 - set_1
    common = set_1 & set_2

    # Преобразуем множества в отсортированные списки
    sorted_unique_1 = sorted(unique_1)
    sorted_unique_2 = sorted(unique_2)
    sorted_common = sorted(common)

    return sorted_unique_1, sorted_unique_2, sorted_common


# Списки стикеров:
stas_collection = [
    "Тим Бернерс-Ли",
    "Линус Торвальдс",
    "Ада Лавлейс",
    "Линус Торвальдс",
    "Маргарет Гамильтон",
    "Бьярн Страуструп",
]
anton_collection = [
    "Тим Бернерс-Ли",
    "Гвидо ван Россум",
    "Линус Торвальдс",
    "Бьярн Страуструп",
    "Бьярн Страуструп",
    "Кен Томпсон",
    "Деннис Ричи",
]

# Вызываем функцию и распаковываем полученный кортеж в три переменные:
stas_stickers, anton_stickers, common_stickers = get_stickers_comparison(
    stas_collection, anton_collection
)

# Печатаем результаты:
print("Стикеры, которые есть только у Стаса:", stas_stickers)
print("Стикеры, которые есть только у Антона:", anton_stickers)
print("Стикеры, которые есть и у Стаса, и у Антона:", common_stickers)
