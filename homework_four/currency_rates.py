from requests import get
import datetime


def currency_rates(name):
    valute = {}
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text.replace('<', '  ').replace('>', '  ')
    response_list = response.split('  ')
    date_list = response_list[3].split('.')
    date = datetime.date(int(date_list[2][:4]), int(date_list[1]), int(date_list[0][-2:]))
    for indx, val in enumerate(response_list):
        if val == 'CharCode':
            valute.update({response_list[indx + 1]: response_list[indx + 13]})
    return valute.get(name.upper(), "None"), date

text = input('Введите наименование валюты : ')
result = currency_rates(text)
print(f'Дата {result[1]} . Курс валюты {text.upper()} по отношению к рублю : {result[0]}')


if __name__ == '__main__':
    import sys