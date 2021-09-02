from itertools import zip_longest
with open('users.csv', 'r') as us, open('hobby.csv','r') as hob:
    names = [i.replace(';', ' ') for i in us.read().splitlines()]           # Создаем список с ФИО, и заменяем разделители ";" на пробелы
    hobbys = [i.replace(';', ',') for i in hob.read().splitlines()]

users_hobbys_gen = ((names,hobbys) for names,hobbys in zip_longest(names,hobbys, fillvalue='None'))


with open('users_hobbys_task_four.txt', 'w',encoding='utf-8') as f:
    for users_hobbys in users_hobbys_gen:
        f.write(f'{users_hobbys[0]} : {users_hobbys[1]}\n')