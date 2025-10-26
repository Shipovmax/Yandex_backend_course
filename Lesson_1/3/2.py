def get_season(month):
    winter = ["декабрь", "январь", "февраль"]
    spring = ["март", "апрель", "май"]  
    summer = ["июнь", "июль", "август"]
    autumn = ["сентябрь", "октябрь", "ноябрь"]
    
    if month in winter:
        return "зима"
    elif month in spring:
        return "весна"
    elif month in summer:
        return "лето"
    elif month in autumn:
        return "осень"
    else:
        return "Ошибка в написании месяца!"

# Тестирование функции
print(get_season("июнь"))      
print(get_season("мартобрь"))  
