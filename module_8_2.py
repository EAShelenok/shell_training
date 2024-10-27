def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы - {i}')
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        if isinstance(numbers, str):
            result = personal_sum(numbers)[0]
        else:
            len_n = 0
            for i in numbers:
                if isinstance(i, int or float):
                    len_n += 1
            result = personal_sum(numbers)[0] / len_n
        return result
    except ZeroDivisionError as exc:
        print(f'Невозможно вычислить среднее арифметическое для пустой коллекции')
        return 0
    except TypeError as exc:
        print(f'Входные данные имеют неверный тип (не коллекция)')
        return None

if __name__ == '__main__':

    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать