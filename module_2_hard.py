num = int(input('Введите число от 3 до 20: '))

password = []
for i in range(1, num):
    for j in range(1, num):
        if num % (i + j) == 0:
            password.append((i, j))
print(*password)