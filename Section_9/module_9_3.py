first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result =(len(first[i]) == len(second[i]) for i in range(len(first)))


print(list(first_result))
print(list(second_result))