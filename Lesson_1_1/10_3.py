from random import randint as rnd 


def get_dumplings_recommendation():
    pelemeny = rnd(10,20)
    return pelemeny

pelemeny = get_dumplings_recommendation()
print('Оптимальным количеством пельменей на сегодня будет', pelemeny)