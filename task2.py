# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

array = list(map(int, input('Введите массив: ').split()))

min_meaning = int(input("Введите минимальное знанчение: "))
max_meaning = int(input("Введите максимальное знанчение: "))

for i in range(len(array)):
    if min_meaning <= array[i] <= max_meaning:
        print(i, end=' ')

