team1_num = 5 #Мастера кода
team2_num = 6 #Волшебники данных
score_1 = 40 #Мастера кода
score_2 = 42 #Волшебники данных
team1_time = 1552.512 #Мастера кода
team2_time = 2153.31451 #Волшебники данных
tasks_total = 82
time_avg = 45.2
challenge_result = ''

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = challenge_result.join('Победа команды Мастера кода!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = challenge_result.join('Победа команды Волшебники Данных!')
else:
    challenge_result = challenge_result.join('Ничья!')

#Использование '%':
print('В команде Мастера кода участников %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

#Использование format():
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {}c!'.format(team2_time))

#Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'{challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')