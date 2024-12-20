def memorize_func(f):
    mem = {}
    def wrapper(*args):
        print(f'Выполнение функции с аргументами = {args}, внутренняя память = {mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась ответ = {mem[args]}'
        else:
            return f'Функция уже была выполнена раньше ответ = {mem[args]}'
    return wrapper

@memorize_func
def func(a, b):
    print(f'Выполняем функцию с аргументами ({a}, {b})')
    return a ** b

#Применяем декоратор к нашей функции.
#Вызываем функцию с разными параметрами

print(func(3, 5))
print(func(3, 5))