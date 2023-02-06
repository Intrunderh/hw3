def CloseNumber(n):
    n = int(input('Введите число, которое хотите найти: '))
    if n < temp[0]:
        return "n меньше всех"
    for i in temp:
        if n < i:
            return x
        x = i
    else:
        return "n больше всех"

import random

a = int(input('Введите количество элементов: '))
temp = []
for i in range(a):
    chisla = int(input('Введите числа: '))
    temp.append(chisla)
print(f'Введенные числа: {temp}')

print(CloseNumber(temp))
