from json import dump
from itertools import zip_longest
with open('users.csv', 'r') as us, open('hobby.csv','r') as hob:
    names = [i.replace(';', ' ') for i in us.read().splitlines()]           # Создаем список с ФИО, и заменяем разделители ";" на пробелы
    hobbys = [i.replace(';', ',') for i in hob.read().splitlines()]         # Создаем список хобби

if len(names) < len(hobbys):
    exit(1)
else :
    user_hobby = dict(zip_longest(names,hobbys, fillvalue='None'))          # Создаем необходимы словарь
    with open('dict(задание 3).txt', 'w',encoding='utf-8') as dic:
        dump(user_hobby,dic, ensure_ascii=False)

