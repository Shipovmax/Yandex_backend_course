def is_palindrome(text):
    # Приводим текст к нижнему регистру и удаляем пробелы
    cleaned_text = text.lower().replace(' ', '')
    
    # Сравниваем строку с её обратной версией с помощью срезов
    return cleaned_text == cleaned_text[::-1]


# Должно быть напечатано True:
print(is_palindrome('А роза упала на лапу Азора'))
# Должно быть напечатано False:
print(is_palindrome('Не палиндром'))