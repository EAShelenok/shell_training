#Рекурсивная функция
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) == 1:
        return first
#Вызовы функции
print(get_multiplied_digits(202004))
#Стек вызовов: get_multiplied_digits(202004) -> 2 * get_multiplied_digits(2004) ->
#-> 2 * 2 * get_multiplied_digits(4) -> 2 * 2 * 4 = 16
print(get_multiplied_digits(405301))
#Стек вызовов: get_multiplied_digits(405301) -> 4 * get_multiplied_digits(5301) ->
#-> 4 * 5 * get_multiplied_digits(301) -> 4 * 5 * 3 * get_multiplied_digits(1) ->
#-> 4 * 5 * 3 * 1 = 60
print(get_multiplied_digits(6203))
#Стек вызовов: get_multiplied_digits(6203) -> 6 * get_multiplied_digits(203) ->
#-> 6 * 2 * get_multiplied_digits(3) -> 6 * 2 * 3 = 36