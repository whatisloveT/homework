list_number = []
final_sum_one = 0
final_sum_two = 0
for i in range(1, 1001):
    if i % 2 != 0:
        list_number.append(i**3)
print(list_number)
for i in list_number:
    sum_number = 0
    for x in str(i):
        sum_number += int(x)
    if sum_number % 7 == 0:
        final_sum_one += i
    sum_number = 0
    i += 17
    for x in str(i):
        sum_number += int(x)
    if sum_number % 7 == 0:
        final_sum_two += i

print(f'Сумма чисел вариант (а)  = {final_sum_one}')
print(f'Сумма чисел вариант (b)  = {final_sum_two}')