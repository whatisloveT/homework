# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    request_list = []
    for line in f:
        remote_addr = line[:line.find(' ')]
        request_type =line[line.find('"')+1:line.find('"')+4]
        requested_resource = line[line.find('/d'):line.find('HTTP')-1]
        request_tuple = (remote_addr,request_type,requested_resource)
        request_list.append(request_tuple)
    print(request_list)