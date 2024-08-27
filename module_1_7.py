grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Создаем переменную - отсортированный список учеников
s_students_list = sorted(list(students))
#Вычисляем средний бал для каждого ученика (с учетом соответствия оценок в списке grades алфавитному порядку учеников)
av_grade_1st = sum(grades[0])/len(grades[0])
av_grade_2nd = sum(grades[1])/len(grades[1])
av_grade_3rd = sum(grades[2])/len(grades[2])
av_grade_4th = sum(grades[3])/len(grades[3])
av_grade_5th = sum(grades[4])/len(grades[4])
#Фомируем словарь, в котором ключ - имя студента, значение - его средний бал
av_st_grades = dict([(s_students_list[0], av_grade_1st),
                     (s_students_list[1], av_grade_2nd),
                     (s_students_list[2], av_grade_3rd),
                     (s_students_list[3], av_grade_4th),
                     (s_students_list[4], av_grade_5th)])
print('Средний бал учеников:', av_st_grades)