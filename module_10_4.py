import threading
from time import sleep
from random import randint
from gevent.queue import Queue


class Table:

    def __init__(self, number):
        self.number = int(number)
        self.guest = None

    def __repr__(self):
        return repr(self.number)

class Guest(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = str(name)

    def run(self):
        sleep(randint(3, 10))

class Cafe:

    def __init__(self, *tables):
        self.qu = Queue()
        self.tables = list(tables)

    def vacant_table(self, tables):
        vacant_tables = []
        for table in tables:
            if table.guest is None:
                vacant_tables.append(table.number)
        return vacant_tables

    def guest_arrival(self, *guests):
        g = []
        if len(self.tables) <= len(guests):
            i = 0
            while i < len(self.tables): #for i in range(len(tables)):
                if self.tables[i].guest is None:
                    self.tables[i].guest = guests[i]
                    guests[i].start()
                    g.append(guests[i])
                    #guests[i].join()
                    print(f'{guests[i].name} сел(-а) за стол номер {self.tables[i]}')
                    i += 1
            if len(self.tables) < len(guests):
                for j in range(len(guests) - len(self.tables) - 2, len(guests)):
                    self.qu.put(guests[j])
                    print(f'{guests[j].name} в очереди')
        else:
            for j in range(len(guests)):
                if self.tables[j].guest is None:
                    self.tables[j].guest = guests[j]
                    guests[j].start()
                    g.append(guests[j])
                    print(f'{guests[j].name} сел(-а) за стол номер {self.tables[j]}')

    def discuss_guests(self):
            while not self.qu.empty() or self.vacant_table(tables) != []:
                for table in self.tables:
                    if table.guest and not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table} свободен')
                        if not self.qu.empty():
                            guest = self.qu.get()
                            table.guest = guest
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table}')
                            guest.start()
                            guest.join()

tables = [Table(number) for number in range(1, 6)]

guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()