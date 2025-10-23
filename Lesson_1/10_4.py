from random import randint as rnd 


def get_dumplings_recommendation(MIN_pelemeny,MAX_pelemeny):
    pelemeny = rnd(MIN_pelemeny,MAX_pelemeny)
    return pelemeny

pelemeny = get_dumplings_recommendation(25,30)
print('Оптимальным количеством пельменей на сегодня будет', pelemeny)