#Команда 1 - Чернокнижники
#Команда 2 - Адепты Света

team1_name = 'Чернокнижники'
team2_name = 'Адепты Света'
team1_num = 5   #Количество участников 1 команды
team2_num = 6   #Количество участников 2 команды
score_1 = 40    #Очки, набранные 1-й командой (кол-во решенных задач)
score_2 = 42    #Очки, набранные 2-й командой (кол-во решенных задач)
team1_time = 1552.512   #Общее время решения задач 1-й командой
team2_time = 2153.31451 #Общее время решения задач 1-й командой

#Общее количество решенных задач
tasks_total = score_1 + score_2
#Общее количество решенных задач
time_avg = round(float((team1_time + team2_time) / tasks_total), 1)   #45.2

if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_num):
    challenge_result = str(f"победа команды '{team1_name}'")
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = str(f"победа команды '{team2_name}'")
else:
    challenge_result = 'ничья'

#Знак  '%'
print("В команде '%s' участников: %s!" % (team1_name, team1_num))
print("В команде '%(name)s' участников: %(count)s!" % {'name': team2_name, 'count': team2_num})
print("Итого сегодня в командах участников: %(team1)s и %(team2)s!" % {'team1': team1_num, 'team2': team2_num})

#Метод format()
print("Команда '{}' решила задач: {}!".format(team2_name, score_2))
print("'{}' решили задачи за {} с!".format(team2_name, round(team2_time, 1)))

#f-строки
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}!")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")

