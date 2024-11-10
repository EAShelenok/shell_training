import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        enemies = 100
        b_day = 0
        print(f'{self.name}, на нас напали! Нужно забороть {enemies} воинов.')
        while enemies > 0:
            time.sleep(1)
            enemies -= self.power
            b_day += 1
            print(f'{self.name} сражается {b_day} день(дня)..., осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {b_day} дня(дней).')

if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    #third_knight = Knight("Sir Wallace", 25)
    first_knight.start()
    second_knight.start()
    #third_knight.start()
    first_knight.join()
    second_knight.join()
    #third_knight.join()
    print('Все битвы закончились!')