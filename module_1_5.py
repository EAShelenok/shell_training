#Кортеж
immutable_var = (3.14, 'Pi', True, 15, 'var', False)
print('Кортеж (immutable tuple):',immutable_var)
#Попытка изменения элементов кортежа приведет к возникновению ошибки, поскольку данный тип данных является неизменяемым,
#т.е., например, выполнение команды immutable_var[2] = False не приведет к положительному результату.
#Однако если в качестве элемента (или элементов) кортежа задать изменяемую структуру (в частности, список), то
#то данный элемент будет доступен для изменения:
immutable_var_wlist = ([3.14, 'Pi', False], 15, 'var', False)
print('Кортеж, содержащий список (immutable tuple with list):', immutable_var_wlist)
immutable_var_wlist[0][2] = True
print('Кортеж c измененным списком (immutable tuple with modified list):', immutable_var_wlist)
#Список
mutable_list = ['torch', 1400, True, 'water', 150.46, False]
print('Список (mutable list):', mutable_list)
mutable_list.append('Physics')
print('Измененный список (append):', mutable_list)
mutable_list.reverse()
print('Измененный список (reverse):', mutable_list)
mutable_list.insert(1,'Thermodynamics')
print('Измененный список (insert):', mutable_list)
mutable_list.remove(False)
print('Измененный список (remove):', mutable_list)
print('Измененный список (slice):', mutable_list[1:len(mutable_list):2])