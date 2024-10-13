from math import pi, sqrt

#Класс Figure
class Figure:
    sides_count = 0                     #атритбут класса

    def __init__(self, color, *sides):              #Конструктор класса задающий атрибуты объекта
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = bool()
        if len(self.__sides) != self.sides_count:   #Проверка корректности введения длин сторон (относительно
            self.__sides = []                       #их количества
            if self.sides_count == 0:
                self.__sides = [1]
            else:
                for i in range(self.sides_count):
                    self.__sides.append(1)

    def get_color(self):                            #метод получения цвета фигуры
        return self.__color

    def __is_valid_color(self, r, g, b):            #метод проверки корректности вводимого цвета фигуры
        correct = False
        if (isinstance(r, int) and (r in range(0, 256)))\
                and (isinstance(g, int) and (g in range(0, 256))) and (isinstance(b, int) and (b in range(0, 256))):
            correct = True
        return correct

    def set_color(self, r, g, b):                   #метод установки нового цвета фигуры
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):                            #метод получения списка длин сторон фигуры
        return self.__sides

    def __is_valid_sides(self, args):               #Метод проверки корректности значений длин сторон
        int_pos = 0
        is_val = False
        for i in args:
            if isinstance(i, int) and i > 0:
                int_pos += 1
        if (len(args) == len(self.__sides)) and (int_pos == len(args)):
            is_val = True
        return is_val

    def __len__(self):                              #метод получения периметра фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):                #метод изменения длин сторон
        if len(list(new_sides)) == self.sides_count and self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

#Класс Circle (дочерний по отношению к Figure)
class Circle(Figure):
    sides_count = 1                                 #атрибут класса (кол-во сторон)

    def __init__(self, col, *sid):                  #конструктор класса
        super().__init__(col, *sid)
        self.radius = len(self) / 2

    def get_square(self):                           #метод вычисления площади круга
        return round(2 * pi * self.radius ** 2, 2)

#Класс Triangle (дочерний по отношению к Figure)
class Triangle(Figure):
    sides_count = 3                                 #атрибут класса (кол-во сторон)

    def get_square(self):                           #метод вычисления площади треугольника
        p = len(self)/2
        abc = self.get_sides()
        tr_sq = sqrt(p * (p - abc[0]) * (p - abc[1]) * (p - abc[2]))
        return round(tr_sq, 2)

#Класс Cube (дочерний по отношению к Figure)
class Cube(Figure):
    sides_count = 12                                #атрибут класса (кол-во сторон)

    def __init__(self, c_col, *c_side):             #конструктор класса, переопределяющий атрибут __sides
        if len(c_side) == 1:
            nc_side = []
            for i in range(self.sides_count):
                nc_side.append(c_side[0])
            super().__init__(c_col, *tuple(nc_side))
        else:
            super().__init__(c_col, *c_side)

    def get_volume(self):                           #метод вычисления объема куба
        return self.get_sides()[0] ** 3

if __name__ == '__main__':

    #Tестовые данные из задания
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    #Дополнительные тестовые данные
    #f1 = Figure((200, 200, 200),20, 10)
    #print(len(f1))
    #print(f1.get_sides())
    #
    #f2 = Circle((200, 200, 200), 4)
    #print(len(f2))
    #print(f2.get_sides())
    #print(f2.radius)
    #print(f2.get_square())
    #
    #f3 = Triangle((255, 224, 100), 4, 4, 4)
    #print(len(f3))
    #print(f3.get_sides())
    #print(f3.get_square())
    #
    #f4 = Cube((200, 100, 50), 3)
    #print(len(f4))
    #print(f4.get_sides())
    #print(f4.get_volume())