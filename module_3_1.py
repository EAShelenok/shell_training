calls = 0
#Функция count_calls
def count_calls():
    global calls
    calls += 1
#Функция string_info
def string_info(user_string):
    leng = len(user_string)
    big_u_string = user_string.upper()
    small_u_string = user_string.lower()
    print(f"Результат работы 'string_info:' {(leng, big_u_string, small_u_string)}")
    count_calls()
#Функция is_contains
def is_contains(ch_string, ch_list):
    if ch_string.lower() in [word.lower() for word in ch_list]:
        contain = True
    else:
        contain = False
    print(f"Результат работы 'is_contains': {contain}")
    count_calls()
#Вызов функций
string_info('January')
string_info('Robust System')
is_contains('Size', ['AuGUst', 'JupiTER', 'SUPER'])
is_contains('ASIa',['EurOpe', 'aSiA', 'Africa'])
print(f"Количество вызовов всех функций: {calls}")