def num_translate(name):
    name_turple = {'Zero' : 'Ноль', 'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре', 'Five' : 'Пять',
                   'Six' : 'Шесть', 'Seven' : 'Семь', 'Eight' : 'Восемь', 'Nine' : 'Девять', 'Ten' : 'Десять', 'zero' : 'ноль',
                   'one' : 'один', 'two' : 'два', 'three' : 'три', 'four' : 'четыре', 'five' : 'пять', 'six' : 'шесть',
                   'seven' : 'семь', 'eight' : 'восемь', 'nine' : 'девять', 'ten' : 'десять', }
    print(name_turple.get(name, 'None'))

text = input('Введите цифру для перевода от 0 до 10 на английском : ')
num_translate(text)
