def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError as exc:
        print('Нельзя складывать разные форматы данных!', exc)
        print(str(a) + str(b))
    except NameError as exc:
        print('Один или несколько параметров не определены. Будь внимательнее!', exc)
    finally:
        return 'Программа завершена'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))