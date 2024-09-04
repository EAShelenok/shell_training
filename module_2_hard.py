import random
#Определим функцию выдачи произвольного числа из заданного диапазона
#(n - начало диапазона; m - конец диапазона)
def get_number(start, stop):
    numbers = list(range(start, stop + 1))
    ch_number = random.choice(numbers)
    print(f'Выпавшее число: {ch_number}')
    return ch_number
#Определим функцию поиска требуемых числовых пар и формирования пароля
def get_pass(number):
    pass_lst = []
    result = ''
    for i in range(1, number):
        for j in range(1, number):
            if (number % (i + j)) == 0 and (i < j):
                pass_lst.append([i, j])
                result += str(i) + str(j)
    print(f'Найденные пары чисел: {pass_lst}')
    print(f'Ваш пароль: {result}')
    return int(result)
#Зададим числовой диапазон и выполним вызов сформированных функций
n = int(input('Введите начальное значение числового диапазона: '))
m = int(input('Введите конечное значение числового диапазона: '))
r_num = get_number(n, m)
get_pass(r_num)