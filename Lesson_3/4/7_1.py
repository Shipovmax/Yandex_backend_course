def fibonacci(n):
    """Создает массив из последовательности чисел Фибоначчи"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


sequence = fibonacci(10)
for number in sequence:
    print(number)
