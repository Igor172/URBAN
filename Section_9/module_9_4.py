import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

equal = list(map(lambda x, y: ord(x) == ord(y), first, second))
print(equal)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


import random
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())