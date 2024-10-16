class Horse:                                            #Класс Horse
    def __init__(self, x_distance = 0, sound = 'Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):                                  #Метод определяющий пройденную дистанцию
        return self.x_distance + dx

class Eagle:                                                                        #Класс  Eagle
    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):                                  #Метод определяющий пройденную дистанцию
        return self.y_distance + dy

class Pegasus(Horse, Eagle):                            #Класс Pegasus, наследующий атрибуты и методы двух предыдущих
    def __init__(self):                                 #классов
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):                             #Метод определения перемещения Pegasus
        self.x_distance = super().run(dx)
        self.y_distance = super().fly(dy)

    def get_pos(self):                                  #Метод получения значения перемещения (координат)
        return (self.x_distance, self.y_distance)

    def voice(self):                                    #Метод вывода издаваемого звука (звук соответствует последнему
        print(self.sound)                               #в цепочки наследований родительскому класса

if __name__ == '__main__':
    #Тестовые данные из задания
    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()