from typing import Any, Union

list_number = []
final_sum_one = 0
final_sum_two = 0
for i in range(1, 1001):
    if i % 2 != 0:
        list_number.append(i**3)
print(list_number)
for i in list_number:
    x = i
    sum_number = 0
    while i != 0:
        sum_number += i % 10
        i = i // 10
    if sum_number % 7 == 0:
        final_sum_one += x
    sum_number = 0
    x += 17
    i = x
    while i != 0:
        sum_number += i % 10
        i = i // 10
    if sum_number % 7 == 0:
        final_sum_two += x

print(f'Сумма чисел вариант (а)  = {final_sum_one}')
print(f'Сумма чисел вариант (b)  = {final_sum_two}')