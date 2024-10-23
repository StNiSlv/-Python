team1_num = 5
result_1 = "В команде Мастера кода участников: %d !" % team1_num
print(result_1)
team2_num = 6
result_2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(result_2)
score_2 = 42
result_3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(result_3)
team1_time = 18015.2
result_4 = "Волшебники данных решили задачи за {:.1f} с !".format(team1_time)
print(result_4)
score_1 = 40
score_2 = 42
result_5 = f"Команды решили {score_1} и {score_2} задач."
print(result_5)
challenge_result = "Победа команды Волшебники данных!"
result_6 = f"Результат битвы: {challenge_result}"
print(result_6)
tasks_total = 82
time_avg = 350.4
result_7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"
print(result_7)
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'
print(challenge_result)
