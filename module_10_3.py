import threading
from random import randint
import time

class Bank:
    def __init__(self):
        self.balance = int()
        self.lock = threading.Lock()
        self.lock.acquire()

    def deposit(self):
        for _ in range(100):
            plus = randint(50, 500)
            self.balance += plus
            print(f'Пополнение: {plus}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)


    def take(self):
        for _ in range(100):
            minus = randint(50, 500)
            print(f'Запрос на: {minus}.')
            if minus <= self.balance:
                self.balance -= minus
                print(f'Снятие: {minus}. Баланс: {self.balance}.')
            else:  #if minus > self.balance:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()

if __name__ == '__main__':
    bk_1 = Bank()
    b_thread_1 = threading.Thread(target=Bank.deposit, args=(bk_1,))
    b_thread_2 = threading.Thread(target=Bank.take, args=(bk_1,))
    b_thread_1.start()
    b_thread_2.start()
    b_thread_1.join()
    b_thread_2.join()
    print(f'Итоговый баланс: {bk_1.balance}')
