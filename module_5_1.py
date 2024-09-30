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

#Создание экземпляров класса
House_1 = House('ЖК Горский', 18)
House_2 = House('Домик в деревне', 2)
House_3 = House('ЖК Весенний', 24)
n_floor_1 = 5
n_floor_2 = 10
n_floor_3 = 15

#Результаты вызовов методов класса для его различных экземпляров
print(f"Жилой комплекс '{House_1.name}', количество этажей: {House_1.number_of_floors}.")
print(f"Жилой комплекс '{House_2.name}', количество этажей: {House_2.number_of_floors}.")
print(f"Жилой комплекс '{House_3.name}', количество этажей: {House_3.number_of_floors}.")
print(f"Попытка подняться на {n_floor_1} этаж в '{House_1.name}':")
House_1.go_to(n_floor_1)
print(f"Попытка подняться на {n_floor_2} этаж в '{House_2.name}':")
House_2.go_to(n_floor_2)
print(f"Попытка подняться на {n_floor_3} этаж в '{House_3.name}':")
House_3.go_to(n_floor_3)