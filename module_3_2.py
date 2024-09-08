#Формируем требуемую функцию
def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    valid_domains = ('.com', '.ru', '.net')
    if not('@' in sender and '@' in recipient) or \
        not(recipient.endswith(valid_domains) and sender.endswith(valid_domains)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}!')
    elif sender == recipient:
        print('Невозможно отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
#Вызываем функцию с различными значениями параметров
send_email('Hello!', 'eleonora@group.ru',sender = 'suppurt_clubdigit.com')
send_email('Cash now!', 'university.help@gmail.com')
send_email('Информационная рассылка университета', 'evgeniy.sh@pnu.com')
send_email('Важное для Вас письмо!', 'julia_s_1980@.net', sender = 'university.plaza@gmail.com')
send_email('Hello!', 'support_now@.pl', sender = 'university.plaza@gmail.com')
send_email('Hello!', 'julia_s_1980@.net')
send_email('Важное для Вас письмо!', 'adam.eva.00@.ru', sender = 'client.info@client.com')