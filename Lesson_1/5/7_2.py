sequence_1 = [69, 59, 57, 60, 63, 44, 46, 69]
sequence_2 = [33, 73, 50, 25, 36, 68, 52, 76]


def compare_sequences(list_1, list_2 ):
    if list_1 > list_2 :
        return f'Список {list_1} больше.'
    elif list_2 > list_1 :
        return f'Список {list_2} больше.'
    elif list_1 == list_2:
        return 'Списки равны.'
    
    
print(compare_sequences(sequence_1, sequence_2))