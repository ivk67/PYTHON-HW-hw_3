# Задача 14.
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите число: '))
k = 1
while k < N:
    print(k)
    k = k * 2
if k < 2:
    print('Вводимое число меньше 2-х')
    