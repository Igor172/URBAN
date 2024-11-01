class Figure:
    sides_count = 0

    def __init__(self, __color, __sides, filled=True):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return [*self.__color]

    def __is_valid_color(self, r, g, b):    # служебный, принимает параметры r, g, b, который проверяет корректность.
        col = (r, g, b)
        for i in col:
            if 0 > i or i > 255:
                return False
        return True

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides) and len(self.__sides) == self.sides_count:
            self.__sides = sides

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):  # служебный, принимает неограниченное кол-во сторон
        for i in sides:
            if i % 1 != 0 or i < 1:
                return False
        return True

    def get_sides(self):  # должен возвращать значение я атрибута __sides.
        if len(self.__sides) == 1:
            return [*self.__sides] * self.sides_count

    def __len__(self):    # должен возвращать периметр фигуры.
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides, filled=True, __radius=0):
        super().__init__(__color, __sides, filled)
        if len(__sides) != self.sides_count:
            self.__sides = 1
        self.__radius = __sides[0] / 6.28

    def get_square(self):
        return (self.__radius ** 2) * 3.14


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides, filled=True, __height=0):
        super().__init__(__color, __sides, filled)
        if len(__sides) != self.sides_count and len(__sides) != 1:
            __sides = [1] * self.sides_count
        elif len(__sides) == 1:
            __sides = [*__sides] * self.sides_count
        else:
            __sides = [*__sides]
        self.__height = ((__sides[0] ** 2) - (__sides[0] / 2) ** 2) ** 0.5

    def get_square(self):
        return self.get_sides()[0] * self.__height / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides, filled=True):
        super().__init__(__color, __sides, filled)
        if len(__sides) != self.sides_count and len(__sides) != 1:
            __sides = [1] * self.sides_count
        elif len(__sides) == 1:
            __sides = [*__sides] * self.sides_count
        else:
            __sides = [*__sides]

    def get_volume(self):
        return self.get_sides()[0] ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())