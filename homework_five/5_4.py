src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
result = [src[i] for i in range(1,len(src)) if src[i] > src[i-1]]  # Создаем список элементов которые больше предыдущего
print(result)                                                      # обязательно попадает в этот список
