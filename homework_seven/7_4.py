"""Данная программа написана самостоятельно с небольшо подсказко по определению ключа в словаре"""

import os
import json

def scan_dir(name):
    name_tuple = {}
    for root, dirs, files in os.walk(name):
        for file in files:
            ext = file.rsplit('.', maxsplit=1)[-1].lower()              # определяем тип файла
            size = os.stat(os.path.join(root, file)).st_size            # определяем размер файла
            len_size = len(str(size))
            key = int('1' + '0' * len_size)                             # создаем верхнюю границу для определния ключа
            if key not in name_tuple:
                name_tuple[key] = [0, []]
            name_tuple[key][0] += 1
            name_tuple[key][1].append(ext)                              # Добавляем тип файла в список
    for key, val in name_tuple.items():                    # Преобразуем списки с типами файлов в списки без повторений
        name_tuple[key][1] = list(set(name_tuple[key][1]))
        name_tuple[key] = tuple(val)                                     # Преобразуем списки значени в кортежи
    with open(f'{name}_summary.json' , 'w', encoding='utf-8') as f:
        json.dump(name_tuple, f, indent=4)
    print(name_tuple)

folder = 'some_data'
scan_dir(folder)
