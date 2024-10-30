def apply_all_func(int_list, *functions):
    r_dict = {}
    for func in functions:
        r_dict[func.__name__] = func(int_list)
    return r_dict

def al_sq(int_list):
    res = []
    for digit in int_list:
        res.append(digit ** 2)
    return res

if __name__ == '__main__':

    #Тестовые данные из задания
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

    #Другие тестовые данные
    print(apply_all_func([34.5, 2.1, 17.7, 190.23], max, min, len, sum, sorted, al_sq))
    print(apply_all_func([3, 2, 7, 12, 5, 4, 1, 11], len, al_sq, max))