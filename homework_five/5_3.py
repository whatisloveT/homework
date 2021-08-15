from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def finish_tuple():
    if len(tutors) < len(klasses):                   # Если длина списка tutors меньше кол-ва классов, то используем zip
        for name, klas in zip(tutors, klasses):      # что бы кол-во генерация было согласно условию, иначе используем
            yield name, klas                         # zip_longest, для наполнения классов отсутствующих
    else:
        for name, klas in zip_longest(tutors, klasses):
            yield name, klas


gen_tuple = finish_tuple()
print(type(gen_tuple))
print(list(gen_tuple))
print(list(gen_tuple))