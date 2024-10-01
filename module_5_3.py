#Определение класса House
class House:
    def __init__(self, name, number_of_floors): #конструктор класса
        self.name = str(name)
        self.number_of_floors = int(number_of_floors)

#Методы класса
    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        if (self.new_floor > self.number_of_floors) or (self.new_floor < 1):
            print(f'Такого этажа не существует!')
        else:
            for floor_num in range(1, self.new_floor + 1):
                print(floor_num)
            print('Успешно!')

#Специальные методы класса (задание module_5_2)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return str(f"Название: '{self.name}', количество этажей: {len(self)}.")

#Дополнительные методы класса (текущее задание)
#Метод проверки совместимости переменных для логических и арифметических операций
    def comp(self, v_op, oper):
        oper_l = ['==', '<', '<=', '!=', '>', '>=']
        oper_a = ['+', '-', '*', '/', '//', '%', '**']
        is_norm = False
        if (isinstance(v_op, House) and (oper in oper_l)) or (isinstance(v_op, int) and (oper in oper_a)):
            is_norm = True
        else:
            print(f"Тип данных одной из переменных не совместим с операцией '{oper}'!")
        return is_norm

#Методы перегрузки операторов сравнения
    def __eq__(self, other):
        if  self.comp(self,  '==') and self.comp(other, '=='):
            return len(self) == len(other)
        else:
            return str(f'Операция не выполнена!')

    def __ne__(self, other):
        if self.comp(self, '!=') and self.comp(other, '!='):
            return len(self) != len(other)
        else:
            return str(f'Операция не выполнена!')

    def __lt__(self, other):
        if self.comp(self, '<') and self.comp(other, '<'):
            return len(self) < len(other)
        else:
           return str(f'Операция не выполнена!')

    def __le__(self, other):
        if self.comp(self, '<=') and self.comp(other, '<='):
            return len(self) <= len(other)
        else:
            return str(f'Операция не выполнена!')

    def __gt__(self, other):
        if self.comp(self, '>') and self.comp(other, '>'):
            return len(self) > len(other)
        else:
            return str(f'Операция не выполнена!')

    def __ge__(self, other):
        if self.comp(self, '>=') and self.comp(other, '>='):
            return len(self) >= len(other)
        else:
            return str(f'Операция не выполнена!')

#Методы перегрузки арифметических операторов
    def __add__(self, value):
        if self.comp(value, '+'):
            self.number_of_floors += value
            return self
        else:
            return str(f'Операция не выполнена!')

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

#Создание экземпляров класса
House_1 = House('ЖК Горский', 18)
House_2 = House('Домик в деревне', 2)
House_3 = House('ЖК Весенний', 18)
House_4 = House('ЖК Эльбрус', 10)
House_5 = House('ЖК Акация', 20)
#n_floor_1 = 5
#n_floor_2 = 10
#n_floor_3 = 15

#__str__
print(str(House_1))
print(str(House_2))
print(str(House_3))
print(str(House_4))
print(str(House_5))

#__len__
#print(f"Высота домов в '{House_1.name}': {len(House_1)} этажа(-ей).")
#print(f"Высота домов в '{House_2.name}': {len(House_2)} этажа(-ей).")
#print(f"Высота домов в '{House_3.name}': {len(House_3)} этажа(-ей).")

print(House_4 == House_5) #__eq__
House_4 = House_4 + 10 #__add__
print(House_4)
print(House_4 == House_5) #__eq__

House_4 += 10 #__iadd_
print(House_4)

House_5 = 10 + House_5 #__radd__
print(House_5)

print(House_4 > House_5) # __gt__
print(House_4 >= House_5) # __ge__
print(House_4 < House_5) # __lt__
print(House_4 <= House_5) # __le__
print(House_4 != House_5) # __ne__

print(str(House_1))
print(str(House_3))
print(House_1 == House_3) #__eq__
House_1 = House_1 + 10 #__add__
print(House_1)
print(House_1 == House_3) #__eq__

House_1 += 10 #__iadd_
print(House_1)

House_3 = 10 + House_3 #__radd__
print(House_5)

print(House_1 > House_3) # __gt__
print(House_1 >= House_3) # __ge__
print(House_1 < House_3) # __lt__
print(House_1 <= House_3) # __le__
print(House_1 != House_3) # __ne__




#Результаты предыдущей задачи (вызовы методов класса)
#print(f"Попытка подняться на {n_floor_1} этаж в '{House_1.name}':")
#House_1.go_to(n_floor_1)
#print(f"Попытка подняться на {n_floor_2} этаж в '{House_2.name}':")
#House_2.go_to(n_floor_2)
#print(f"Попытка подняться на {n_floor_3} этаж в '{House_3.name}':")
#House_3.go_to(n_floor_3)