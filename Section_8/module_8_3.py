class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin):
        if not isinstance(self.__vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        elif self.__vin < 1000000 or self.__vin > 10000000:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

  try:
      second = Car('Model2', 300, 'т001тр')
  except IncorrectVinNumber as exc:
      print(exc.message)
  except IncorrectCarNumbers as exc:
      print(exc.message)
  else:
      print(f'{second.model} успешно создан')

  try:
      third = Car('Model3', 2020202, 'нет номера')
  except IncorrectVinNumber as exc:
      print(exc.message)
  except IncorrectCarNumbers as exc:
      print(exc.message)
  else:
      print(f'{third.model} успешно создан')