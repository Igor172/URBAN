import inspect

import requests
from pandas import set_option
from pandas.io.formats.printing import pprint_thing

'''Интроспекция - это способность объекта во время выполнения получить тип, доступные аттрибуты и методы, а также другую 
информацию, необходимую для выполнения дополнительных операций с объектом'''

some_string = 'i am a string'
some_number = 42
some_list = [some_string, some_number]


def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)


class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()

func = some_function

#Пример 1 - Аттрибут класса __name__

'''print(some_function.__name__)
print(SomeClass.__name__)
print(requests.__name__)
print(func.__name__)'''
#print(some_string.__name__)  выведет ошибку, т.к. данные встроенные функции не имеют подобного метода и работают иначе
#print(some_number.__name__)  выведет ошибку, т.к. данные встроенные функции не имеют подобного метода и работают иначе

# Пример 2 - узнаем тип объекта

'''print(type(some_number))
print(type(some_number) is int)
print(type(some_number) is list)

print(type(requests))
print()'''


# Пример 3 - функция dir
#Функция dir возвращает отсортированный список аттрибутов и методов, доступных для указанного объекта, который может
# быть объявленной переменной или функцией.

from pprint import pprint

'''pprint(dir(some_number))
print()
pprint(dir(some_list))
print()
pprint(dir(some_function))
print()
pprint(dir(SomeClass))
print()
pprint(dir(some_object))
print()
pprint(dir(requests))'''

#Без указания аргумента dir() выводит доступные в локальной области видимости, как показано ниже.

#Пример 4 - функция hasattr() - проверка на наличие существования аттрибута

'''attr_name = 'attribute_2'
print(hasattr(some_object, attr_name))
print(hasattr(some_object, 'attribute_1'))
pprint(dir(some_object))

# Пример 5 - функция getattr - получение аттрибута

print(getattr(some_object, 'attribute_1')) #Проверяем значение аттрибута
print(getattr(some_object, 'attribute_2', 'Этого не может быть')) # В случае отсутствия аттрибута, задаем что вернуть.
# Если не задать вывод, то выведет ошибку AttributeError

#Выведем структурированно все имеющиеся методы и аттрибуты

for attr_name in dir(requests):
    attr = getattr(requests, attr_name)
    print(attr_name, type(attr))'''


#Пример 6 - функция callable() - проверка на то,можем ли мы вызывать этот объект
'''
print(callable(some_string))
print(callable(some_function))
print(callable(some_object.attribute_1))
print(callable(some_object.some_class_method))

#Пример 7 - функция isinstance() - мы можем определить, является ли определенный объект экземпляром указанного класса

print(isinstance(some_number, str))
print(isinstance(some_number, int))
print(isinstance(some_number, SomeClass))
print(isinstance(some_object, SomeClass))'''

#Пример 8 - модуль inspect - собирает удобные методы и классы для отображения интроспективной информации
# Самые употребимые функции

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.isbuiltin(requests))

some_function_module = inspect.getmodule(some_function) # Проверяет из какого модуля мы взяли наш объект
print(type(some_function_module), some_function_module)















