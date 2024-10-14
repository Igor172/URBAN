import math

class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=True):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        return all(side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):

    sides_count = 1

    def __init__(self, color, radius, filled=False):
        super().__init__([2 * math.pi * radius], color, filled)
        self.__radius = radius

    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):

    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):

    sides_count = 12

    def __init__(self, color, side_length, filled=False):
        super().__init__([side_length] * 12, color, filled)

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
