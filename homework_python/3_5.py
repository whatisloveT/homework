from random import choice
def get_jokes(number, repeat = False):
    """
    Функция которая создает шутки из заданых списков
    :param number: колличество повторений шуток
    :param repeat: оператор отвечающий за повтор слов в шутках. По умолчанию повтор разрешен
    :return: None
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(number):
        temp_nouns =choice(nouns)                           # Присваиваем временной переменной рандомный элемент из первого списка
        temp_adverbs = choice(adverbs)                      # Присваиваем временной переменной рандомный элемент из первого списка
        temp_adjectives = choice(adjectives)                # Присваиваем временной переменной рандомный элемент из первого списка
        print(f'{temp_nouns} {temp_adverbs} {temp_adjectives}')     #Выводим на печать шутку из рандомных элементов заданных списков
        if repeat :
            nouns.remove(temp_nouns)
            adverbs.remove(temp_adverbs)
            adjectives.remove(temp_adjectives)
get_jokes(5,True)