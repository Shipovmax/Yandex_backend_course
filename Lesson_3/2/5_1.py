class Product:
    def __init__(self, name, many):
        self.name = name
        self.many = many

    def get_info(self):
        return f'{self.name} (в наличии: {self.many})'


class Kettlebell(Product):
    def __init__(self, name, many, weight):
        super().__init__(name, many)
        self.weight = weight
    
    def get_weight(self):
        return f'{Product.get_info(self)}. Вес: {self.weight} кг'


class Clothing(Product):
    def __init__(self, name, many, size):
        super().__init__(name, many)
        self.weight = size
    
    def get_size(self):
        return f'{Product.get_info(self)}. Размер: {self.weight}'


small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())