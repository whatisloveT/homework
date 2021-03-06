def thesaurus_adv(*args):
    dictionary_of_names = {}
    for i in args:
        surname = i.split()[-1]                                  # Вводим переменную фамилии
        dictionary_of_names.setdefault(surname[0],{})            # Создаем словарь с ключем перво буквы фамилии и значением пустого словаря
        dictionary_of_names[surname[0]].setdefault(i[0],[])      # Создаем словарь внитри словаря с ключем первой буквы имени и значением списком
        dictionary_of_names[surname[0]][i[0]]+=[i]               # Добавляем в этот список фамилию и имя
    return dictionary_of_names
# print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
#                    "Илья Иванов", "Анна Савельева", "Наталья Романова", "Линара Акушкина",
#                    "Евгений Времянкин", "Евгений Скрашевский"))

"Далее прописана реализация сортировки по ключам"
a = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                    "Илья Иванов", "Анна Савельева", "Наталья Романова", "Линара Акушкина",
                    "Евгений Времянкин", "Евгений Скрашевский")
list_keys = list(a.keys())    # Создаем список из ключей исходного словаря
list_keys.sort()              # Сортируем его
for i in list_keys:           # Выводим значения по списку отсортированных ключей из исходного словаря
    print(i, ':', a[i])
