def planting_plan(rows):
    listok = []
    for i in range(2,2*rows+1,2):
        listok.append(i)
    return listok

print(planting_plan(5))