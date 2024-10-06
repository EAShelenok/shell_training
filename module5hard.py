from time import sleep

#Класс User
class User:
    cr_user = list()
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)
        self.cr_user = [self.nickname, self.password, self.age]

    def check_age(self):
        if self.age >= 18:
            ok_pass = True
        else:
            ok_pass = False
        return ok_pass

    def u_pass(self):
        return self.password

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return  repr(self.cr_user)

# Класс Video
class Video:
    cr_video = list()
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)
        self.cr_video = [self.title, self.duration, self.time_now, self.adult_mode]

    def v_duration(self):   #Метод определения продолжительности воспроизведения
        return range(self.time_now + 1, self.duration + 1)

    def v_start_time(self): #Метод сброса времени начала воспроизведения
        self.time_now = 0
        return self.time_now

    def v_cens(self):
        return self.adult_mode

    def __repr__(self):
        return repr(self.cr_video)

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
       return str(self.title)

    def __len__(self):
        return self.duration

# Класс UrTube
class UrTube:
    def __init__(self):  # Конструктор класса
        self.users = list() # список пользователей
        self.videos = list()
        self.current_user = None

    def check_nick(self, nickname):  # Метод проверки повторяющегося имени пользователя
        nick_ex = False
        for i in self.users:
            if nickname in str(i):
                nick_ex = True
                break
        return nick_ex

    def check_pass(self, nickname, password):  #Метод сравнения имени пользователя и пароля
        pass_ex = False
        a = self.users
        for i in self.users:
            if nickname == str(i) and hash(password) == User.u_pass(i):
                pass_ex = True
                self.current_user = i
                break
        return pass_ex

    def log_in(self, nickname, password): # Метод входа пользователя
        if self.check_nick(nickname) and self.check_pass(nickname, password):
            print(f"Успешный вход пользователя '{self.current_user}'")
        #else:
        #    print(f'Неверное имя пользователя и/или пароль')

    def log_out(self):  #  Метод выхода (сброс текущего пользователя)
        print(f"Пользователь '{self.current_user}' вышел из системы")
        self.current_user = None

    def add(self, *args):
        if self.videos == []:
            videos_tmp = [args[i] for i in range(len(args))]
            for i in videos_tmp:
                if i not in self.videos:
                    self.videos.append(i)
        else:
            for i in args:
                if i not in self.videos:
                    self.videos.append(i)

    def get_videos(self, s_word):
        g_vid = []
        for i in self.videos:
            if s_word.lower() in str(i).lower():
                g_vid.append(str(i))
        return g_vid

    def register(self, nickname, password, age):  # Метод регистрации пользователя
        if self.check_nick(nickname):
            print(f"Пользователь '{nickname}' уже существует.")
        else:
            r_user = User(nickname, password, age)
            self.users.append(r_user)
            print(f"Пользователь '{r_user.nickname}' успешно зарегистрирован.")
            self.log_in(nickname, password)

    def watch_video(self, v_title):
        if self.current_user == None:
            print(f'Войдите в аккаунт, чтобы смотреть видео!')
        else:
            for i in self.videos:
                if  str(i) == v_title:
                    if (Video.v_cens(i) and User.check_age(self.current_user)) or not Video.v_cens(i):
                        for t in Video.v_duration(i):
                            print(str(t), end = ' ')
                            sleep(1)
                        print('Конец видео')
                        Video.v_start_time(i)
                    else:
                        print(f'Вам нет 18 лет, пожалуйста покиньте страницу!')

if __name__ == '__main__':
    ur = UrTube()
    #Примеры из задания
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    #Иные тестовые данные
    #Регистрация пользователей
    #ur.register('Vasiliy Androsov', 'Darkness123', 10)
    #ur.register('Ivan Petrov', 'IsTrUeUser0328', 39)
    #ur.register('Vasiliy Androsov', 'Issue_2', 10)
    #
    ##Попытки входа в аккаунты
    #ur.log_in('Vasiliy Androsov', 'Darkness123')  #успешный
    #ur.log_in('Vasiliy Androsov', 'd')  #неуспешный
    #
    ##Создание объектов класса Video и их добавление в объект класса UrTube
    #v1 = Video('Лучший язык программирования 2024 года', 200)
    #v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)
    #v3 = Video('Призраки долины снов', 300, 10, True)
    #v4 = Video('Призраки долины снов', 4)
    #v5 = Video('Лучший язык программирования 2024 года', 150)
    #v6 = Video('Призраки долины снов', 4, adult_mode = True)
    #ur.add(v1, v2, v3, v4, v5, v6)
    #v7 = Video('Адская кухня', 500, 0, adult_mode=True)
    #v8 = Video('Some Kind of Monster', 10, 3, True)
    #ur.add(v7, v8)
    #v9 = Video('Some Kind of Monster', 10, 0)
    #ur.add(v9)
    #
    ##Проверка поиска видео
    #print(ur.get_videos('лучший'))
    #print(ur.get_videos('ПРОГ'))
    #
    ##Вывод текущего пользователя
    #print(ur.current_user)
    #
    ##Попытка просмотра видео. Неуспешное - пользователю нет 18 лет
    #ur.watch_video('Some Kind of Monster')
    #
    ##Выход из системы
    #ur.log_out()
    #
    ##Попытка просмотра видео
    #ur.watch_video('Some Kind of Monster')  #Неуспешное - ни один пользователь не вошел в систему
    #
    ##Вход в систему другого пользователя (старше 18 лет)
    #ur.log_in('Ivan Petrov', 'IsTrUeUser0328')
    #print(ur.current_user)
    #ur.watch_video('Some Kind of Monster')
    #ur.watch_video('Some Kind of Monster')