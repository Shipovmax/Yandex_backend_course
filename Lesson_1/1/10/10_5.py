# Эта функция должна возвращать слово Hello 
def say_hello():
    return 'Hello'


# Эта функция должна возвращать строку "World!" (с восклицательным знаком).
def say_world():
    return 'World!'

# В переменной result должна быть фраза Hello, World!
# А функция print() должна вывести эту фразу на экран.
result = str(say_hello()) + ', ' + str(say_world())
print(result)