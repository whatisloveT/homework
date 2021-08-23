
""" К сожалению самостоятельно справиться с заданием мне не удалось,
 воспользовался помощью одного из одногруппников, и просто разобрался в коде. """

import json
import os
import sys


def scan_conf(your_conf, cur_dir=os.path.dirname(__file__)):
    for dir_name in your_conf:
        os.mkdir(os.path.join(cur_dir, dir_name))
        if not your_conf[dir_name]:
            continue

        new_path = os.path.join(cur_dir, dir_name)

        for el in your_conf[dir_name]:
            print(el)
            if type(el) is dict:
                scan_conf(el, new_path)

            else:
                with open(os.path.join(new_path, el), 'w', encoding='utf-8'):
                    pass


with open('config.json', 'r', encoding='utf-8-sig') as f:
    conf = json.load(f)

if os.path.isdir(str(list(conf.keys())[0])):
    print('Такая папка проекта уже существует. Проверьте и запустите скрипт заново.')
    sys.exit(1)

scan_conf(conf)
print('Каталог проекта создан.')
