from random import choice

#Lamdba-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(f'Пример работы Lamdba-функции:')
print(list(map(lambda ch_1, ch_2: ch_1 == ch_2, first, second)))

#Замыкание
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for item in data_set:
                file.write(str(item) + '\n')

    return write_everything

print("Для проверки работы закмыкания откройте файл 'example.txt'")
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__
class Mystic_Ball:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

print("Пример использования магического метода '__call__':")
first_ball = Mystic_Ball('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())