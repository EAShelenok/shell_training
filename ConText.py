class Context:

    def __init__(self):
        self.values = tuple()

    def get_val(self):
        return self.values

    def __enter__(self):
        self.__n = self.values
        self.values = list(self.values)
        return self.values

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.values = self.__n
            raise Exception
        else:
            self.values = tuple(self.values)
        return self.values

if __name__ == '__main__':
    
    #Первый экземпляр
    cm = Context()
    print(cm.values)
    try:
        with cm as list_:
            list_.append((2.3, 10, 59))
            list_.append('String')
    except Exception:
        pass
    print(cm.values)
    try:
        with cm as list_:
            list_.append([200, 'Years'])
            list_.append(3)
            list_.append('Class')
    except Exception:
        pass
    print(cm.values)
    
    #Второй экземпляр
    cm_1 = Context()
    print(cm_1.values)
    try:
        with cm_1 as list_1:
            list_1.append('New String')
            list_1.append(33.6)
    except Exception:
        pass
    print(cm_1.values)
    try:
        with cm_1 as list_1:
            list_1.append('New String_2')
            list_1.hg(3)
    except Exception:
        pass
    print(cm_1.values)

    #Третий экземпляр
    cm_2 = Context()
    print(cm_2.values)
    try:
        with cm_2 as list_2:
            list_2.append([[2, 3, 4],'New String 2'])
            list_2.append((45, 30))
    except Exception:
        pass
    print(cm_2.values)
    try:
        with cm_2 as list_2:
            list_2.scb(3)
            list_2.append((45, 30))
    except Exception:
        pass
    print(cm_2.values)
