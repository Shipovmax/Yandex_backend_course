def assess_yield(number_of_plants, average_weight):
    radis = float(number_of_plants * average_weight / 1000)

    if radis > 100:
        return radis, "Ожидается отличный урожай."
    elif radis <= 100 and radis > 50:
        return radis, "Ожидается хороший урожай."
    elif radis > 0 and radis <= 50:
        return radis, "Урожай будет так себе."
    else:
        return radis, "Урожая не будет."


total_weight, rating = assess_yield(50, 200)
print(total_weight, "кг.", rating)
