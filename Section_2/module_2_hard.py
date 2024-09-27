num = int(input('Введите число от 3 до 20: '))

password = []
for i in range(1, num):
    for j in range(1, num):
        if num % (i + j) == 0 and i <= j:
            password.append((i, j))

for pair in password:
    print(*pair, end=' ')