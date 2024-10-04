
class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.houses_history.append(args[0])
        return obj

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        elif 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        isinstance(other, int)
        return self.number_of_floors == other

    def __lt__(self, other):
        isinstance(other, int)
        return self.number_of_floors < other

    def __le__(self, other):
       isinstance(other, int)
       return self.number_of_floors <= other

    def __gt__(self, other):
        isinstance(other, int)
        return self.number_of_floors > other

    def __ge__(self, other):
        isinstance(other, int)
        return self.number_of_floors >= other

    def __ne__(self, other):
        isinstance(other, int)
        return self.number_of_floors != other

    def __add__(self, value):
        isinstance(value, int)
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        isinstance(value, int)
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        isinstance(value, int)
        self.number_of_floors += value
        return self



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)