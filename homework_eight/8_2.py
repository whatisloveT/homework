import re
import json
re_ip = re.compile(r'^(([\d\w]{0,4}[\.:]){3,7}[\d\w]{1,4})') # регулярное выражения для определения ip в том числе и формата 2001:4802:7801:103:8bee:6e66:ff20:475c
request_datetime = re.compile(r'\[([^\[]+)\]')    # выражение для нахождения даты
request_type = re.compile(r'"([A-Z]{3})')         # выражение для определения типа
requested_resource = re.compile(r' (/\w+/\w+_\d+)')      # выражение для пути
response_coder = re.compile(r'" ([0-9]{1,}) ')           # выражение для определения кода
response_size =re.compile(r' ([0-9]{1,}) "')             # выражение для определения размера
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        sought_set = ((re_ip.search(line).group()),request_datetime.findall(line)[0],\
                      request_type.search(line).group(),requested_resource.search(line).group(), \
                      response_coder.search(line).group(),response_size.search(line).group()\
                      )
        print(sought_set)