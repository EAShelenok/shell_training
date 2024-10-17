def custom_write(file_name, strings):
    str_num = 0
    string_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        str_num += 1
        cur_pos = file.tell()
        file.write(i + "\n")
        string_positions[(str_num, cur_pos)] = i
    file.close()
    return string_positions

if __name__ == '__main__':

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)