def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    global count_num
    count_num = 0
    try:
        for num in numbers:
            if isinstance(num, (int, float)):
                result += num
                count_num += 1
            else:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчета суммы - {num}')
        raise TypeError
    except TypeError:
        return result, incorrect_data

def calculate_average(numbers):
    global count_num
    try:
        result, incorrect_data = personal_sum(numbers)
        if len(numbers) == 0:
            raise TypeError
        average = result / count_num
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В {numbers} записан некорректный тип данных.')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать