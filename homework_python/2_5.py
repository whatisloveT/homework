def print_price(name):
    for i in name:
        print(f'{int(i)} руб. {int((i * 100) % 100):02d} коп.',
              end=', ')  # Выводим список цен переведенных в руб. и коп.
    print(f'\nid списка = {id(name)}')
price_list = [33.33, 57, 120.3, 97.25, 58.49, 113.3, 153.4, 45.53, 3.50, 14.38, 76.34]
# Вариант А
print_price(price_list)
#Вариант В
price_list.sort()  #Сортируем список по возрастанию
print_price(price_list)
#Вариант С
price_list.reverse()   #Отсортированны список переворачиваем и получаем список по убываанию цены
print_price(price_list)
#Вариант D
print_price(price_list[:5]) #Выводим первые 5 самых дорогих товаров