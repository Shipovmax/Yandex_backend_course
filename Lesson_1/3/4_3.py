def find_pool_capacity(num_of_people, length, width=None):
    if length < 0:
        length = -length
    if num_of_people < 0:
        num_of_people = -num_of_people

    if width is None:
        area = length * length
    elif width < 0:
        area = length * -width
    else:
        area = length * width

    if num_of_people / area <= 2:
        print(
            "Бассейн площадью "
            + str(area)
            + " кв. м. вмещает "
            + str(num_of_people)
            + " чел."
        )
    else:
        print(
            "Бассейн площадью "
            + str(area)
            + " не вмещает "
            + str(num_of_people)
            + " чел."
        )


find_pool_capacity(4, 2)
find_pool_capacity(4, 5, 10)
find_pool_capacity(-10, -5, -2)
find_pool_capacity(25, 5, 2)
