import io
import requests
import datetime
import pandas as pan
import json
import matplotlib.pyplot as plt

#Задача: запросить данные о курсах валют с использованием API (api.apilayer.com), записать данные по курсам с первого
#до текущего дня текущего месяца в файлы с именами 'rates_list_year-month-date.txt'. Считать данные из полученных
#файлов, сформировать список из дата-фреймов курсов валют. Вывести график изменения соответствующего курса за
#исследуемый период.

#Используем библиотеку requests для запроса необходимых данных
#Создадим функцию для считывания данных о курсах валют; в качестве базовой валюты используем евро, запрашиваем стоимость
#одного евро в долларах и рублях. Аргумент функции - дата.

def write_file_from_url(date):
    SYMBOLS = 'RUB,USD' #параметр, указывающий на запрашивамую стоимость относительно базовой валюты
    BASE = 'EUR'        #параметр, задающий базовую валюту
    API_KEY = '5xPAl9kqOIS4TDMZGvrAyCvldNrCP81G' #ключ доступа к API (cработает на 100 запросов, 22 уже потратил =))
    headers = {'apikey': API_KEY}                   #параметр для передачи в метод request
    url_date = f'https://api.apilayer.com/fixer/{date}?symbols={SYMBOLS}&base={BASE}'   #ссылка запроса
    with open(f'rates_list_{date}.txt', 'w', encoding='utf-8') as file:     #запрашиваем данные за введенную дату
        curr_list_date = requests.request('GET', url_date, headers=headers) #и записываем результат в файл
        file.write(curr_list_date.text)                                             #с соответствующим именем

#Создадим функцию для считывани данных из файла с именем 'file_name'
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        template = json.load(file)
    return template

if __name__ == '__main__':

    #формируем пул дат начиная с первого до текущего числа текущего месяца
    st_date = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, 1) #начальная дата
    en_date = datetime.datetime.now().date()                                                     #конечная дата

    #запускаем цикл запросов данных и записи результатов в файлы
    for i in range(int((en_date - st_date).days) + 1):
        write_file_from_url(st_date + datetime.timedelta(i))
        print(f'Запрашиваем данные за {st_date + datetime.timedelta(i)}')

    #печать содержимого одного из файлов
    print('Содержимое одного из сформированных фaйлов:', '\n', read_file(f'rates_list_{st_date}.txt'))

#Библиотека pandas (формируем список дата-фреймов счет считывания данных из полученных файлов)
    d_frames = list()
    for i in range(int((en_date - st_date).days) + 1):
        try:
            f_name = io.StringIO(f'rates_list_{st_date + datetime.timedelta(i)}.txt')
            d_frames.append(pan.read_json(f_name.getvalue()))
        except ValueError:                              #сработает, если отсутствует файл за какую-либо дату из пула
            print(f'Данные за {st_date + datetime.timedelta(i)} не найдены. Работаем без них...')

    #вывод полученного списка дата-фреймов
    print(d_frames)

#Библиотека mathplotlib (строим график изменения стоимости евро за исследуемый период)
#формируем значения дат (x_f) и стоимостей (x_y)
    try:
        x_r_f = []
        y_r_f = []
        x_d_f = []
        y_d_f = []
        for i in d_frames:
            x_r_f.append(i['date']['RUB'])
            y_r_f.append(i['rates']['RUB'])
            x_d_f.append(i['date']['USD'])
            y_d_f.append(i['rates']['USD'])

        #строим график изменения евро в рублях
        plt.subplot(1, 2, 1)
        plt.plot(x_r_f, y_r_f)
        plt.title('Курс Евро-Рубль')
        plt.xlabel('Дата')
        plt.ylabel('Стоимость Евро в Рублях')
        plt.grid(True)
        plt.subplot(1, 2, 2)
        plt.plot(x_d_f, y_d_f)
        plt.title('Курс Евро-Доллар')
        plt.xlabel('Дата')
        plt.ylabel('Стоимость Евро в Долларах')
        plt.grid(True)
        plt.show()
    except Exception:     #На случай если не будет данных на текущую дату (из-за разницы в часовых поясах)
        pass