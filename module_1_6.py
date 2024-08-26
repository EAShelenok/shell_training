#Словарь (Имя, возраст)
my_dict = {'Evgeniy': 38, 'Maxim': 26, 'Anatoliy': 60, 'Asya': 32}
print('Исходный словарь:',my_dict)
print('Значение по существующему ключу (Maxim):',my_dict.get('Maxim'))
print('Значение по отсутвующему ключу (Anton):',my_dict.get('Anton','Такого ключа не существует!'))
my_dict.update({'Anton': 24,
                'Irina': 50})
d_val = my_dict.pop('Anton')
print('Значение из удаленной пары:',d_val)
print('Измененный словарь:',my_dict)
#Множество
my_set = {1, 12, 'Adaptive', 445.4, 12, 'Evgeniy', 1}
print('Исходное множество:', my_set)
my_set.add((2, 'Robust'))
my_set.add(3.14)
my_set.discard('Adaptive')
print('Измененное множество:', my_set)