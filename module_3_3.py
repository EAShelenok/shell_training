#Функция print_params
def print_params(a = 2, b = 'Вывод', c = False):
    print(a, b, c)
#Вызовы функции. В случае использования позиционных параметров со значениями по умолчанию
#можно передать в функцию либо все аргументы, либо их меньшее количество (включая вызов без аргументов).
#Если требуется передать часть параметров, порядок следования которых не совпадает с порядком в функции,
# то необходимо указать их имя.
#Примеры вызова функции print_param
print_params(10, 'Задание', False)
print_params(a = 'Super', c = 500)
print_params()
print_params(b = 2)
print_params(c = [1, 2, 3])
print_params(10, 2)
#Список и словарь
values_list = ['Строка из списка', True, 959]
values_dict = {'a': False, 'b': 878, 'c': 'Строка из словаря'}
#Передача параметров в функцию print_param из списка и словаря
print_params(*values_list)
print_params(**values_dict)
#Список с двумя параметрами
values_list_2 = [777, 'Два параметра']
#Передача параметров из values_list_2 в функцию print_params
print_params(*values_list_2, 42)
print_params(545, *values_list_2)