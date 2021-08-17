def num_translate():
    text = input('Введите цифру для перевода от 0 до 10 на английском : ')
    if text.istitle():
        print(name_turple.get(text.lower()).title())
    else :
        print(name_turple.get(text))

name_turple = {'zero' : 'ноль', 'one' : 'один', 'two' : 'два', 'three' : 'три', 'four' : 'четыре', 'five' : 'пять',
                   'six' : 'шесть', 'seven' : 'семь', 'eight' : 'восемь', 'nine' : 'девять', 'ten' : 'десять'}
num_translate()