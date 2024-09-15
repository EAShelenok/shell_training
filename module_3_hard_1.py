#Формируем функцию подсчета суммы цифр и длин строк в заданной структуре данных
from time import struct_time


def calculate_structure_sum(*in_struct):
    sum_digit = 0
    sum_char = 0
    first = in_struct[0]
#Сформируем вложенную функцию подсчета суммы элементарных единиц структуры (целых чисел и длин строк)
#за счет рекурсивных вызовов для каждого уровня вложенности элемента входной структуры (аналог обхода деревьев)
        if isinstance(in_struct[item], set) or isinstance(in_struct, tuple) or isinstance(in_struct, list):
            for i in in_struct:
            calculate_structure_sum(i)
    elif isinstance(in_struct, dict):
        for k, v in in_struct.items():
            calculate_structure_sum(k)
            calculate_structure_sum(v)
    elif isinstance(in_struct, int):
        sum_digit += in_struct
    else:
        sum_char += len(in_struct)
    return sum_digit + sum_char
#Повторяем вызов вложенной функции для следующего элемента основной (входной) структуры
    #calculate_structure_sum(in_struct[1])
    #return sum_digit + sum_char

#Зададим структуры данных для передачи в созданную функцию
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

data_structure_2 = [
    1,
    [2, 'help',  {'Фамилия': 'Иванов'}, {1, 'py'}, 2],
    [3, 1, (1, 5, 2)]
]

data_structure_3 = [
    {'Error': 'None'},
    1
]

data_structure_4 = (
    (3, 10),
    ['Dogshelter']
)

#Вызовы функции
print(f'Заданная структура данных: {data_structure}')
result_1 = calculate_structure_sum(data_structure)
print(f'Сумма чисел и длин строк структуры: {result_1}')
print(f'Заданная структура данных: {data_structure_2, data_structure_3}')
result_2 = calculate_structure_sum(data_structure_2, data_structure_3)
print(f'Сумма чисел и длин строк структуры: {result_2}')
print(f'Заданная структура данных: {data_structure_4}')
result_3 = calculate_structure_sum(data_structure_4)
print(f'Сумма чисел и длин строк структуры: {result_3}')