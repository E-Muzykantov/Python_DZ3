# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X . 
# Если таких значений больше одного, вывести первый найденный.

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

lenght_array = int(input('Введите размер массива: '))
array = [randint(1, 10) for i in range(lenght_array)]
print(array)
number = int(input('Введите искомое число: '))
array_difference = [abs(i - number) for i in array]
print(array[array_difference.index(min(array_difference))])