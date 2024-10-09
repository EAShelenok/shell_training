class Vehicle:                                                  #Класс Vehicle (родительский)
    __COLOR_VARIANTS = ['White', 'Black', 'Grey', 'Metallic']   #атрибут класса, содержащий доступные для
                                                                #изменения цвета
    def __init__(self, owner, model, color, engine_power):      #конструктор класса задающий атрибуты объекта класса
        self.owner = str(owner)
        self.__model = str(model)
        self.__color = str(color)
        self.__engine_power = int(engine_power)

class Sedan(Vehicle):               #Класс Sedan (дочерний по отношению к Vehicle)
    _PASSENGERS_LIMIT = 5           #Атрибут класса, соответствующий максимальной вместимости седана

    def get_model(self):                                #метод возврата модели седана (обращение к атрибуту объекта,
        return str(f"Модель: {self._Vehicle__model}")   #созданного в родительском классе)

    def get_horsepower(self):                                                   #метод возврата мощности двигателя
        return str(f"Мощность двигателя: {self._Vehicle__engine_power} л.с.")   #седана

    def get_color(self):                                #Метод возврата цвета седана
        return str(f"Цвет: {self._Vehicle__color}")

    def print_info(self):                   #метод вывода информации об автомобиле
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner} \n")

    def set_color(self, new_color):                                             #метод смены цвета автомобиля
        print(f"Пытаемся сменить цвет {self._Vehicle__model} на {new_color}")
        if new_color.lower() in str(self._Vehicle__COLOR_VARIANTS).lower():
            self._Vehicle__color = new_color
            print('Успешное изменение цвета')
        else:
            print(f"Нельзя сменить цвет на {new_color}!")

if __name__ == '__main__':
    #Тестовые данные из задания
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()

    #Дополнительные тестовые данные
    v_1 = Sedan('Evgeniy', 'Prius', 'Black',98)
    v_2 = Sedan('Asya', 'C-HR', 'Grey', 109)
    v_1.print_info()

    v_1.set_color('pink')
    v_1.set_color('GREY')
    v_1.owner = 'Anatoliy'
    v_1.print_info()

    v_2.print_info()
    v_2.set_color('Marsala')
    v_2.set_color('Black')
    v_2.owner = 'Asya Aleksandrovna'
    v_2.print_info()