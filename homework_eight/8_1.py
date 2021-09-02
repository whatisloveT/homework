# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
# почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.

import re


def email_parse(email):
    mail = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$') #Регулярное выражение для определнеия email адреса
    username = re.compile(r'^[a-zA-Z0-9_.+-]+')                     # Регулярное выражение для определения имени
    domain = re.compile(r'[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$')      # Регулярное выражение для определения домена
    try:
        if mail.match(email):                # если email корректны то сосздаем словарь иначе выводим нужную нам ошибку
            email_tuple = {'username': username.findall(email)[0], 'domain': domain.findall(email)[0]}
            print(email_tuple)
        else:
            raise ValueError
    except ValueError:
        print(f'ValueError: wrong email: {email}')


text = input('Введите Ваш email: ')
email_parse(text)
