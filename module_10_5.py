from multiprocessing import Process, Pool
from time import time

def read_info(name):
    all_data = list()
    with open(name, 'r', encoding='utf-8') as file:
        while file.readline():
            all_data.append(file.readline())

if __name__ == '__main__':

    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

    st_time = time()
    for name in filenames:
        read_info(name)
    en_time = time()
    print('Время работы программы при линейном вызове:', round(en_time - st_time, 2), 'сек.')

    #Убрать комментарии для запуска процессов
    #st_time_2 = time()
    #with Pool(4) as testdrive:
    #    testdrive.map(read_info, filenames)
    #en_time_2 = time()
    #print('Время работы программы при многопроцесности:', round(en_time_2 - st_time_2, 2), 'сек.')


