import datetime
from decimal import Decimal


def add(items, title, amount, expiration_date=None):
    # Преобразуем expiration_date в datetime.date если указан
    if expiration_date:
        expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()
    
    # Создаем словарь для новой партии продукта
    new_batch = {
        'amount': Decimal(str(amount)),
        'expiration_date': expiration_date
    }
    
    # Если продукт уже есть в словаре, добавляем к существующему списку
    if title in items:
        items[title].append(new_batch)
    else:
        # Если продукта нет, создаем новый список
        items[title] = [new_batch]


def add_by_note(items, note):
    parts = note.split()
    
    # Минимально должно быть название и количество
    if len(parts) < 2:
        return
    
    # Пробуем найти дату в конце строки
    expiration_date = None
    amount_str = parts[-1]
    
    # Проверяем, является ли последняя часть датой
    try:
        datetime.datetime.strptime(amount_str, '%Y-%m-%d')
        # Если это дата, то количество - предпоследняя часть
        amount_str = parts[-2]
        expiration_date = parts[-1]
        # Название - все части кроме двух последних
        title = ' '.join(parts[:-2])
    except ValueError:
        # Если последняя часть не дата, то срока годности нет
        expiration_date = None
        # Название - все части кроме последней
        title = ' '.join(parts[:-1])
    
    # Добавляем продукт
    add(items, title, amount_str, expiration_date)


def find(items, needle):
    needle_lower = needle.lower()
    result = []
    
    for title in items.keys():
        if needle_lower in title.lower():
            result.append(title)
    
    return result


def amount(items, needle):
    total = Decimal('0')
    needle_lower = needle.lower()
    
    for title, batches in items.items():
        if needle_lower in title.lower():
            for batch in batches:
                total += batch['amount']
    
    return total