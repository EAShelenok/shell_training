import threading
import time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(word_count):
            file.write(f'Какое-то слово № {word + 1}\n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл '{file_name}'.")

st_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
en_time = time.time()
print(f'Работа функций: {round(en_time - st_time, 1)} сек.')

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
n_threads = [thread_1, thread_2, thread_3, thread_4]
st_time_1 = time.time()
for m_thread in n_threads:
    m_thread.start()
for m_thread in n_threads:
    m_thread.join()
en_time_1 = time.time()
print(f'Работа потоков: {round(en_time_1 - st_time_1, 1)} сек.')