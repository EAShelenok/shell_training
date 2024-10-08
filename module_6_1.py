#Класс Animal
class Animal:
    alive = True                #атрибуты класса
    fed = False
    def __init__(self, name):   #конструктор класса, задающий название животного (при создании дочерних классов
        self.name = name        #Mammal или Predator)

#Класс Plant
class Plant:
    edible = False              #атрибут класса
    def __init__(self, name):   #конструктор класса, задающий название животного (при создании дочерних классов
        self.name = name        #Flower или Fruit)

#Класс Mammal (дочерний по отношению к классу Animal)
class Mammal(Animal):
    def eat(self, food):                                    #метод проверки "съедобности"
        if isinstance(food, Fruit):
            print(f"{self.name} съел {food.name}")
            self.fed = True                                 #переопределение значения родительского атрибута
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False                              #переопределение значения родительского атрибута

#Класс Predator (дочерний по отношению к классу Animal)
class Predator(Animal):
    def eat(self, food):                                    #метод проверки "съедобности"
        if isinstance(food, Fruit):
            print(f"{self.name} съел {food.name}")
            self.fed = True                                 #переопределение значения родительского атрибута
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False                              #переопределение значения родительского атрибута

#Класс Flower (дочерний по отношению к классу Plant)
class Flower(Plant):
    pass

#Класс Fruit (дочерний по отношению к классу Plant)
class Fruit(Plant):
    edible = True           #переопределение значения родительского атрибута

if __name__ == '__main__':
    #Тестовые данные из задания
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)

    #Дополнительные тестовые данные
    a3 = Predator('Амурский тигр')
    a4 = Mammal('Дельфин')
    p3 = Flower('Болеголов')
    p4 = Fruit('Ананас')

    print(a3.name)
    print(p4.name)

    print(a3.alive)
    print(a3.fed)
    a3.eat(p4)
    a4.eat(p3)
    print(a3.alive)
    print(a4.fed)
    print(a4.alive)