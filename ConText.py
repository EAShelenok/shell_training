class Context:
    __n_val = None

    def __init__(self):
        self.values = tuple()

    def __enter__(self):
        self.__n_val = list(self.values)
        return self.__n_val

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.values = tuple(self.__n_val)
        return self.values

if __name__ == '__main__':

    cm = Context()
    print(cm.values)
    with cm as list_:
        list_.append((2.3, 10, 59))
        list_.append('String')
    print(cm.values)
    with cm as list_1:
        list_1.append(200)
    print(cm.values)

    cm_1 = Context()
    print(cm_1.values)
    with cm_1 as list_:
        list_.append('New String')
    print(cm_1.values)

    cm_2 = Context()
    print(cm_2.values)
    with cm_2 as list_:
        list_.append([[2, 3, 4],'New String 2'])
        list_.append((45, 30))
    print(cm_2.values)