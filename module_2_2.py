first = int(input('Введите первое число: '))
second = int(input('Введите первое число: '))
third = int(input('Введите первое число: '))
print('Введенные числа: ' + str(first)+ ', ' + str(second) + ', ' + str(third))
if (first == second and second != third) or (first != second and second == third)  or (first != second and first == third):
    print('Количество равных чисел:', 2)
elif first == second and second == third:
    print('Количество равных чисел:', 3)
else:
    print('Количество равных чисел:', 0)