text = int(input('Введите число : '))
num_gen = (num for num in range(1 ,text + 1 , 2))
print(num_gen)
print(list(num_gen))