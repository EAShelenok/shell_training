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

#Специальные методы класса
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return str(f"Название: '{self.name}', количество этажей: {self.number_of_floors}.")

#Создание экземпляров класса
House_1 = House('ЖК Горский', 18)
House_2 = House('Домик в деревне', 2)
House_3 = House('ЖК Весенний', 24)
n_floor_1 = 5
n_floor_2 = 10
n_floor_3 = 15

#__str__
print(str(House_1))
print(str(House_2))
print(str(House_3))

#__len__
print(f"Высота домов в '{House_1.name}': {len(House_1)} этажа(-ей).")
print(f"Высота домов в '{House_2.name}': {len(House_2)} этажа(-ей).")
print(f"Высота домов в '{House_3.name}': {len(House_3)} этажа(-ей).")

#Результаты предыдущей задачи (вызовы методов класса)
print(f"Попытка подняться на {n_floor_1} этаж в '{House_1.name}':")
House_1.go_to(n_floor_1)
print(f"Попытка подняться на {n_floor_2} этаж в '{House_2.name}':")
House_2.go_to(n_floor_2)
print(f"Попытка подняться на {n_floor_3} этаж в '{House_3.name}':")
House_3.go_to(n_floor_3)