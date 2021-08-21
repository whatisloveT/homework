# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.

with open('nginx_logs.txt', 'r') as f:
    remote_addr_list = [line[:line.find(' ')] for line in f]


spam_ip = max(set(remote_addr_list),key=remote_addr_list.count)
print(spam_ip, remote_addr_list.count(spam_ip))