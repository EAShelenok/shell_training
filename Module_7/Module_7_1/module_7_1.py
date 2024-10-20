class Product():
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')

class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file_r = open(self.__file_name, 'r')
        content = file_r.read()
        file_r.close()
        return content

    def add(self, *products):
        for i in products:
            #n_prod = str(i)[: str(i).find(',')]            #Удалить комментарий для проверки "строго по названию",
            if str(i) in self.get_products():               #заменить str(i) на n_prod,
                print(f"Продукт '{i}' уже есть в магазине") #заменить i на n_prod
            else:
                file_a = open(self.__file_name, 'a')
                file_a.write(str(i) + '\n')
                file_a.close()

if __name__ == '__main__':
    #Тестовые данные из задания
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    s1.add(p1, p2, p3)
    print(s1.get_products())
