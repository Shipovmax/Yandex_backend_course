bash = 31
c_and_c_plus_plus = 29
c_sharp = 11
html_css = 36
java = 19
javascript = 37
sql = 34
value = [bash,c_and_c_plus_plus,c_sharp,html_css,java,javascript,sql]

def analyze_skills():
    print('Доля питонистов, у которых есть наименее популярный навык (в %):', min(value))
    print('Доля питонистов, у которых есть наиболее популярный навык (в %):', max(value))

# Не удаляйте вызов функции.
analyze_skills()