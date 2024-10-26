def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    global mount_num
    mount_num = 0
    try:
        for num in numbers:
            if isinstance(num, (int, float)):
                result += num
                mount_num += 1
            else:
                raise TypeError
    except TypeError as exc:
        incorrect_data += 1
        print(f'Некорректный тип данных {exc} для подсчета суммы - {incorrect_data}')
    return result, incorrect_data

def calculate_average(numbers):
    global mount_num
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        if len(numbers) == 0:
            raise ZeroDivisionError
        average = total_sum / mount_num
        return average
    except ZeroDivisionError as exc:
        return 0
    except TypeError as exc:
        print(f'В {numbers} записан некорректный тип данных. {exc}')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать