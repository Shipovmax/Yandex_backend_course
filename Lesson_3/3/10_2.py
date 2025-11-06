from datetime import datetime
from random import sample


def choose_days():
    # Определяем диапазон дат первой половины месяца.
    first_month_half = list(range(1, 16))  # от 1 до 15 включительно

    # Выбор трёх случайных чисел:
    random_days = sample(first_month_half, k=3)
    # Cортировка этих чисел по возрастанию:
    sorted_days = sorted(random_days)

    # Получаем сегодняшнюю дату.
    # На её основе будут генерироваться даты для занятий:
    now = datetime.now()

    # Чтобы было проще формировать сообщение, начнём цикл с 0 до 2.
    for i in range(3):
        try:
            # Генерируем дату занятия, подменяя номер дня в сегодняшней дате.
            practice_day = now.replace(day=sorted_days[i]).strftime("%d.%m.%Y")
            print(f"{i + 1}-е занятие: {practice_day}")
        except ValueError:
            # Если день не существует в текущем месяце (маловероятно для 1-15)
            # выбираем другой день
            alternative_days = [d for d in first_month_half if d not in sorted_days]
            if alternative_days:
                new_day = sample(alternative_days, 1)[0]
                sorted_days[i] = new_day
                sorted_days.sort()
                practice_day = now.replace(day=new_day).strftime("%d.%m.%Y")
                print(f"{i + 1}-е занятие: {practice_day}")


choose_days()
