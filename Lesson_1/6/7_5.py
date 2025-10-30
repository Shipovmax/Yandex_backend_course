def get_competition_data(data):
    # Собираем все уникальные названия команд из всех заездов
    teams = set()
    for race in data:
        teams.update(race.keys())
    
    # Сортируем команды по алфавиту
    sorted_teams = sorted(teams)
    
    # Формируем строку с перечислением команд
    teams_string = ", ".join(sorted_teams)
    
    # Выводим список команд
    print(f"Команды, участвовавшие в гонке: {teams_string}")
    
    # Шаг 1: Собираем итоговые баллы по всем заездам
    scores = {}
    for race in data:
        for team, score in race.items():
            if team not in scores:
                scores[team] = 0
            scores[team] += score
    
    # Шаг 2: Поиск победителя
    winner_team = None
    winner_score = 0
    
    for team, score in scores.items():
        if score > winner_score:
            winner_score = score
            winner_team = team
    
    # Выводим победителя
    print(f"В гонке победила команда {winner_team} с результатом {winner_score} баллов")

races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]

get_competition_data(races_data)