# Использование %:
team1_num = 5
string1 = "В команде Мастера кода участников: %d !" % team1_num
print(string1)

team2_num = 6
string2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(string2)

# Использование format():
score_2 = 42
string3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(string3)

team1_time = 18015.2
string4 = "Волшебники данных решили задачи за {} с !".format(team1_time)
print(string4)


team2_time = 10717.6
string4 = "Волшебники данных решили задачи за {} с !".format(team2_time)
print(string4)


# Использование f-строк:
score_1 = 40
string5 = f"Команды решили {score_1} и {score_2} задач."
print(string5)

challenge_result = "победа команды Мастера кода!"
string6 = f"Результат битвы: {challenge_result}"
print(string6)

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / 82
string7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!"
print(string7)
