from datetime import datetime

def get_results(time_winner_vhod, time_first_vhod):
    
    time_winner = datetime.strptime(time_winner_vhod, '%H:%M:%S')
    time_first = datetime.strptime(time_first_vhod, '%H:%M:%S')
    
    if time_first != time_winner:
        result = time_first - time_winner 
        # Форматируем время для вывода только часов, минут и секунд
        time_first_str = time_first.strftime('%H:%M:%S')
        time_winner_str = time_winner.strftime('%H:%M:%S')
        print('Вы пробежали за', time_first_str, 'с отставанием от лидера', result)
    else:
        time_winner_str = time_winner.strftime('%H:%M:%S')
        print('Вы пробежали за', time_winner_str, 'и победили!')

# Проверьте работу программы, можете подставить свои значения.
get_results('02:02:02', '02:02:02')
get_results('02:02:02', '03:04:05')