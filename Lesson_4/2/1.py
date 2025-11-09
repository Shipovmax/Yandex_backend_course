import requests

url = "http://wttr.in/?0T"

response = requests.get(url)  # правильно выполняем HTTP-запрос

print(response.text)  # печатаем текст HTTP-ответа
