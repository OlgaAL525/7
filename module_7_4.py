
team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 1552.512
team2_time = 2153.31451

Task_total = score_1 + score_2
time_avg = round((team1_time + team1_time)/Task_total, 1)

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and (team1_time/score_1) < (team2_time/score_2):
        result = 'победа команды Мастера кода'
    elif score_1 < score_2 or score_1 == score_2 and (team1_time/score_1) > (team2_time/score_2):
        result = 'победа команды Волшебники данных'
    else:
        result = 'Ничья'
    return result

print('В команде Мастера кода участников: %s' %'5' )
print('Итого сегодня в командах участников: %s и %s' % (5, 6))

print('Команда Волшебники данных решила задач:{}'.format(score_2))
print('Волшебники данных решили задачи за: {} секунд!'.format(team2_time))

print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {challenge_result()}')
print(f'Сегодня было решено {Task_total} задач, в среднем по {time_avg} секунды на задачу!')